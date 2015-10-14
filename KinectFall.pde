import KinectPV2.KJoint;
import KinectPV2.*;

import gab.opencv.*;
import processing.video.*;
import java.awt.*;

OpenCV opencv;
KinectPV2 kinect;
Skeleton [] skeleton;

void setup() {
  size(1920, 1080);
  
  kinect = new KinectPV2(this);
  
  kinect.enableSkeleton(true);
  kinect.enableSkeletonColorMap(true);
  
  kinect.enableColorImg(true);
  kinect.init();
   
  opencv = new OpenCV(this, 1920, 1080);
}

void draw() {
    
   opencv.loadImage(kinect.getColorImage());
  PImage img = opencv.getInput();
 image(img,0,0); 
   skeleton =  kinect.getSkeletonColorMap();
   // Get individual jonts
   for (int i = 0; i < skeleton.length; i++) {
     if (skeleton[i].isTracked()) {
       KJoint[] joints = skeleton[i].getJoints();
       
       // Joints of interest are the elbows and hips if the elbows are lower than the hips a fall has occurred
       
       
       // Right Hip
       float xrh = joints[kinect.JointType_HipRight].getX();
       float yrh = joints[kinect.JointType_HipRight].getY();
       ellipse(xrh,yrh,50,50);
       
       // Left Hip
       float xlh = joints[kinect.JointType_HipLeft].getX();
       float ylh = joints[kinect.JointType_HipLeft].getY();
       ellipse(xlh,ylh,50,50);
       
       // Right Knee
       float xrk = joints[kinect.JointType_KneeRight].getX();
       float yrk = joints[kinect.JointType_KneeRight].getY();
       ellipse(xrk,yrk,50,50);
       
       // Left Knee
       float xlk = joints[kinect.JointType_KneeLeft].getX();
       float ylk = joints[kinect.JointType_KneeLeft].getY();
       ellipse(xlk,ylk,50,50);
       
       color col = getIndexColor(i);
       fill(col);
       stroke(col);
       drawBody(joints);
       
       drawHandState(joints[KinectPV2.JointType_HandRight]);
       drawHandState(joints[KinectPV2.JointType_HandLeft]);
       float dstandr = yrk - yrh;
       float dstandl = ylk - ylh;
      
      if (dstandr > 150 || dstandl > 150) {
        println("Standing");
      }
      if (dstandr < 50 || dstandl < 50) {
        println("Falling");
      }
     // println("dstandr = ",dstandr);
      //println("dstandl = ",dstandl);
      
     }
   }
} 
   

   


// get color index
color getIndexColor(int index) {
  color col = color(255);
  if (index == 0)
    col = color(255, 0, 0);
  if (index == 1)
    col = color(0, 255, 0);
  if (index == 2)
    col = color(0, 0, 255);
  if (index == 3)
    col = color(255, 255, 0);
  if (index == 4)
    col = color(0, 255, 255);
  if (index == 5)
    col = color(255, 0, 255);

  return col;
}

  // Draw Body function
 void drawBody(KJoint[] joints) {
  drawBone(joints, KinectPV2.JointType_Head, KinectPV2.JointType_Neck);
  drawBone(joints, KinectPV2.JointType_Neck, KinectPV2.JointType_SpineShoulder);
  drawBone(joints, KinectPV2.JointType_SpineShoulder, KinectPV2.JointType_SpineMid);
  drawBone(joints, KinectPV2.JointType_SpineMid, KinectPV2.JointType_SpineBase);
  drawBone(joints, KinectPV2.JointType_SpineShoulder, KinectPV2.JointType_ShoulderRight);
  drawBone(joints, KinectPV2.JointType_SpineShoulder, KinectPV2.JointType_ShoulderLeft);
  drawBone(joints, KinectPV2.JointType_SpineBase, KinectPV2.JointType_HipRight);
  drawBone(joints, KinectPV2.JointType_SpineBase, KinectPV2.JointType_HipLeft);

  // Right Arm    
  drawBone(joints, KinectPV2.JointType_ShoulderRight, KinectPV2.JointType_ElbowRight);
  drawBone(joints, KinectPV2.JointType_ElbowRight, KinectPV2.JointType_WristRight);
  drawBone(joints, KinectPV2.JointType_WristRight, KinectPV2.JointType_HandRight);
  drawBone(joints, KinectPV2.JointType_HandRight, KinectPV2.JointType_HandTipRight);
  drawBone(joints, KinectPV2.JointType_WristRight, KinectPV2.JointType_ThumbRight);

  // Left Arm
  drawBone(joints, KinectPV2.JointType_ShoulderLeft, KinectPV2.JointType_ElbowLeft);
  drawBone(joints, KinectPV2.JointType_ElbowLeft, KinectPV2.JointType_WristLeft);
  drawBone(joints, KinectPV2.JointType_WristLeft, KinectPV2.JointType_HandLeft);
  drawBone(joints, KinectPV2.JointType_HandLeft, KinectPV2.JointType_HandTipLeft);
  drawBone(joints, KinectPV2.JointType_WristLeft, KinectPV2.JointType_ThumbLeft);

  // Right Leg
  drawBone(joints, KinectPV2.JointType_HipRight, KinectPV2.JointType_KneeRight);
  drawBone(joints, KinectPV2.JointType_KneeRight, KinectPV2.JointType_AnkleRight);
  drawBone(joints, KinectPV2.JointType_AnkleRight, KinectPV2.JointType_FootRight);

  // Left Leg
  drawBone(joints, KinectPV2.JointType_HipLeft, KinectPV2.JointType_KneeLeft);
  drawBone(joints, KinectPV2.JointType_KneeLeft, KinectPV2.JointType_AnkleLeft);
  drawBone(joints, KinectPV2.JointType_AnkleLeft, KinectPV2.JointType_FootLeft);

  drawJoint(joints, KinectPV2.JointType_HandTipLeft);
  drawJoint(joints, KinectPV2.JointType_HandTipRight);
  drawJoint(joints, KinectPV2.JointType_FootLeft);
  drawJoint(joints, KinectPV2.JointType_FootRight);

  drawJoint(joints, KinectPV2.JointType_ThumbLeft);
  drawJoint(joints, KinectPV2.JointType_ThumbRight);

  drawJoint(joints, KinectPV2.JointType_Head);
}

void drawJoint(KJoint[] joints, int jointType) {
  pushMatrix();
  translate(joints[jointType].getX(), joints[jointType].getY(), joints[jointType].getZ());
  ellipse(0, 0, 25, 25);
  popMatrix();
}

void drawBone(KJoint[] joints, int jointType1, int jointType2) {
  pushMatrix();
  translate(joints[jointType1].getX(), joints[jointType1].getY(), joints[jointType1].getZ());
  ellipse(0, 0, 25, 25);
  popMatrix();
  line(joints[jointType1].getX(), joints[jointType1].getY(), joints[jointType1].getZ(), joints[jointType2].getX(), joints[jointType2].getY(), joints[jointType2].getZ());
}

void drawHandState(KJoint joint) {
  noStroke();
  handState(joint.getState());
  pushMatrix();
  translate(joint.getX(), joint.getY(), joint.getZ());
  ellipse(0, 0, 70, 70);
  popMatrix();
}

 // Draw Hand States function 
 void handState(int handState) {
  switch(handState) {
  case KinectPV2.HandState_Open:
    fill(0, 255, 0);
    break;
  case KinectPV2.HandState_Closed:
    fill(255, 0, 0);
    break;
  case KinectPV2.HandState_Lasso:
    fill(0, 0, 255);
    break;
  case KinectPV2.HandState_NotTracked:
    fill(255, 255, 255);
    break;
  }
}

 
  //PImage img = opencv.getInput();
  //image(img, 0, 0);


