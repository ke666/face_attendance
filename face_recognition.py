import cv2
import sys
import pathlib
import os
sys.path.append(os.path.abspath(pathlib.Path(__file__).parent.absolute()))
import glob
import numpy as np
import cv2
import tensorflow as tf
import time
from mtcnn_master.mtcnn.mtcnn import MTCNN
from facenet_face_recognition_master.fr_utils import *
from facenet_face_recognition_master.inception_blocks_v2 import *
from keras import backend as K


#create triploss function
def triplet_loss(y_true, y_pred, alpha = 0.3):
    anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]

    pos_dist = tf.reduce_sum(tf.square(tf.subtract(anchor,
               positive)), axis=-1)
    neg_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, 
               negative)), axis=-1)
    basic_loss = tf.add(tf.subtract(pos_dist, neg_dist), alpha)
    loss = tf.reduce_sum(tf.maximum(basic_loss, 0.0))
   
    return loss



#define database
def prepare_database():
    database = {}


    for folder in glob.glob("facenet_face_recognition_master/images/*"):
        for file in glob.glob(folder+"/*"):
           identity = os.path.splitext(os.path.basename(file))[0]
           database[identity] = img_path_to_encoding(file, FRmodel)

    return database

#define recog function
def who_is_it(image, database, model):
    encoding = img_to_encoding(image, model)
    
    min_dist = 100
    identity = None
    
    # Loop over the database dictionary's names and encodings.
    for (name, db_enc) in database.items():
        dist = np.linalg.norm(db_enc - encoding)
        print('distance for %s is %s' %(name, dist))
        if dist < min_dist:
            min_dist = dist
            identity = name
    
    if min_dist > 0.6:
        return Un_k
    else:
        identity=identity.split("_")[0]
        return identity

def stop_program():
    if cap.isOpened():
        cap.release()


def main():
    detector = MTCNN()
    K.set_image_data_format('channels_first')
    global FRmodel
    global Un_k
    global cap
    FRmodel = faceRecoModel(input_shape=(3, 96, 96))

    FRmodel.compile(optimizer = 'adam', loss = triplet_loss, metrics = ['accuracy'])
    load_weights_from_FaceNet(FRmodel)

    Un_k="unknown"

    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255, 255, 255)
    thickness = 2


    #call database func
    data=prepare_database()

    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, image = cap.read()
        result = detector.detect_faces(image)
        
        for person in result:
            bounding_box = person['box']
            keypoints = person['keypoints']
            cv2.rectangle(image,
                          (bounding_box[0], bounding_box[1]),
                          (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                          (0,155,255),
                          2)
            crop_img = image[bounding_box[1]:bounding_box[1]+bounding_box[3], bounding_box[0]:bounding_box[0] + bounding_box[2]]

             #call recog func
            id=who_is_it(crop_img, data, FRmodel)
            image=cv2.putText(image,id,(bounding_box[0],bounding_box[1]),font,  
                           fontScale, color, thickness, cv2.LINE_AA)
            image=cv2.putText(image,"Press Q to quit",(50,50),font,  
                           fontScale, color, 1, cv2.LINE_AA)
            print (id)
        cv2.imshow("FACE ATTENDANCE SYSTEM",image)
        print(time.perf_counter())


        # Display the resulting frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    
