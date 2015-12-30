#!/usr/bin/python3
import os.path
import os
import argparse
#file_name = "~/path/to/data"
#input_file = "/path/to/file.mp3"
#output_dir = "/tmp/out"


def getSec(a):
    returnValue = 0
    for index, i in enumerate(a):
        if index == 0:
            returnValue += int(i) * 60 * 60.0
        if index == 1:
            returnValue += int(i) * 60.0
        if index == 2:
            returnValue += int(i)
        if index == 3:                
            returnValue += int(i)/1000.0
    return returnValue
def multiply_string(a, b = 0.0):
    
    returnValue = getSec(a) - b
    
    returnValue *= 2
    hours = int(returnValue / (60 * 60))
    returnValue = str("%.2d" % hours) + ":" + str("%.2d" % int(returnValue / 60  - hours * 60)) + ":" + str(int(returnValue % 60)) + "."  + str(int(returnValue % 1 * 1000))
    return str(returnValue)


def split_audio_file(file_name, input_file, output_dir):
    data = []
    for line in open(file_name):
        if line.startswith("Chapter"):
            chapter_info = line.strip().split()
            number = chapter_info[1][:-1]
            time_index_start = chapter_info[2]
            data.append({"number": number, "time_index_start": time_index_start})
        if line.startswith("Total Dur"):
            track_end = line.strip().split()[3]
    for index, chapter in enumerate(data):
        if len(data) > index + 1:
            chapter_end = data[index + 1]["time_index_start"]
        else:
            chapter_end = track_end
            
        chapter_start = chapter["time_index_start"]
        
        
        print(chapter_start)
        
        chapter_end = multiply_string(chapter_end.split(":"), getSec(chapter_start.split(":")))
        chapter_start = multiply_string(chapter_start.split(":"))
        
        
        
        number = int(chapter["number"])
        print(str(number) + ":" + chapter_start + "-" + chapter_end)
        output_file = os.path.join(output_dir, "Chapter_%.2d.mp3" % number)
        command = "ffmpeg -i " + input_file + "  -vn -acodec copy -ss " + chapter_start + " -t " + chapter_end + " " + output_file
        print(command)
        os.system(command)
    return

def handleArgs():
    """ Handle input flags """
    parser = argparse.ArgumentParser(add_help=True, description='Split an mp3 encoded with AAX2MP3 based on an AAXchapters2.0 output file')
    parser.add_argument('file_name', type=str,
                help='The file data from AAX chapters 2.0')
    parser.add_argument('input_file', type=str,
                help='The mp3 file')
    parser.add_argument('output_dir', type=str,
                help='The output folder, should be created')
    args = parser.parse_args()
    return args, parser

if __name__ == "__main__":
    import sys
    args, _ = handleArgs()
    print(args)
    split_audio_file(args.file_name, args.input_file, args.output_dir)
    
    
    
