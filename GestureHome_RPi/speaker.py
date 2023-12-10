import os

import pygame

# Initializations
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

# Access Music
music_folder = "/home/pi/project2/song_list"
music_files = [f for f in os.listdir(music_folder)]
print(music_files)
print(music_files[0])
print(type(music_files[0]))

# Set initial values & Load the first song
current_track_index = 0
paused = False
volume = 0.5
current_track = os.path.join(music_folder, music_files[current_track_index])
pygame.mixer.music.load(current_track)
pygame.mixer.music.set_volume(volume)

# Functions for controlling music


def next_track():
    global current_track_index, paused
    current_track_index = (current_track_index + 1) % len(music_files)
    load_and_play()


def prev_track():
    global current_track_index, paused
    current_track_index = (current_track_index - 1) % len(music_files)
    load_and_play()


def load_and_play():
    global paused
    current_track = os.path.join(
        music_folder, music_files[current_track_index])
    pygame.mixer.music.load(current_track)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    paused = False


running = True
load_and_play()
pygame.mixer.music.pause()
last_num = -1
while running:
    with open('audio.txt', 'r') as file:
        last_line = file.readlines()[-1]
        if last_line != last_num:
            print(str(last_line))
            last_num = last_line
            if str(last_line) == 'pause\n':
                print('now pausing')
                pygame.mixer.music.pause()
            elif str(last_line) == 'play\n':
                print('now playing')
                pygame.mixer.music.unpause()
            elif str(last_line) == 'next\n' or str(last_line) == 'nextnext\n':
                next_track()
            elif str(last_line) == 'prev\n' or str(last_line) == 'prevprev\n':
                prev_track()
            elif str(last_line) == 'clean\n':
                pygame.mixer.music.pause()
            elif str(last_line)[0] == 'v':
                print(last_line)
                volume = int(last_line[1:3])
                print(float(volume)/100)
                pygame.mixer.music.set_volume(float(volume)/100)

pygame.quit()
