# Import emotion_detector and unittest
from emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_tector(self):
        # Test case for joy
        result_1 = emotion_detector('I am glad this happened')
        #print(result_1)
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case for anger
        result_2 = emotion_detector('I am really mad about this')
        #print(result_2)
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        
        # Test case for disgust
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        #print(result_3)
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test case for sadness
        result_4 = emotion_detector('I am so sad about this')
        #print(result_4)
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Test case for fear
        result_5 = emotion_detector('I am really afraid that this will happen')
        #print(result_5)
        self.assertEqual(result_5['dominant_emotion'], 'fear')

unittest.main()