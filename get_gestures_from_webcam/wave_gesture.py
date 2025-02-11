from datetime import datetime


class WaveGesture(object):
    def __init__(self):
        self.temporary_wave_gestures = []
        self.last_hand_x_position = 0
        self.wave_frames = 0
        self.wave_gesture_time = datetime.now()

    def get_wave_gesture(self, landmarks_x, landmarks_y):
        this_hand_x_position = landmarks_x[8]
        # print(abs(self.last_hand_x_position - this_hand_x_position))
        if abs(self.last_hand_x_position - this_hand_x_position) > 0.15:
            self.temporary_wave_gestures.append(True)
            self.last_hand_x_position = this_hand_x_position
        else:
            self.wave_frames += 1
        # print("temporary {} and wave_frames {}".format(len(self.temporary_wave_gestures), self.wave_frames))
        # If we found 7 wave gestures in the last max 20 frames where no wave was made.
        if len(self.temporary_wave_gestures) == 7:
            aux_frames = self.wave_frames
            self.wave_frames = 0
            self.temporary_wave_gestures = []
            if aux_frames < 20:
                return True

        return False
