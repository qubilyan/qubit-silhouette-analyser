
# Qubit Silhouette Analyser

This repository provides a detailed comparison of DeepLabv3, FCN, MOG2, and GMG in the context of extracting human silhouettes from videos. Three different videos were analyzed whereby the ResNet-101-based models were used to semantically segment human pixels in each frame, resulting in a silhouette binary mask. Binary maps from manual rotoscoping were utilized as a ground truth to generate a confusion matrix, thereby producing the mean F-score.

A series of images and tables are included in the README to provide visual support to the test results and specific details involving each method's process. Also detailed here is the typical process for most algorithms achieving silhouette extraction, an explanation of the custom test dataset used in the report, and an explanation of the functions involved in the process.

The Results section provides an overview of the accuracy of each method, with accompanying images to illustrate distribution of FPS, accuracy by method, and speed versus accuracy. A concluding section summarizes the findings and provides direction for potential areas of further research.

The README wraps up with a thorough list of references for further reading and understanding.

**This project was established and maintained by qubilyan. Please feel free to use, improve, build upon, shout-out, blame or critique this work, ultimately for the purpose of improving and furthering research and understanding of human silhouette extraction in the open source community.**