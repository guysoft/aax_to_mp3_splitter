# Aax to MP3 Splitter
Take mp3 files created from AAX2MP3, and text created from AudibleChapters and split accordingly

USE THIS FOR BACKUP ONLY.
Software and anything in this repo is provided provided AS IS.

#Usage
##You will need
1. Audible account with YOUR books, download a book from Audible website.
2. AAXtoMP3 http://sourceforge.net/projects/aaxtomp3/
3. AudibleChapters https://www.hydrogenaud.io/forums/index.php?showtopic=83362
4. Script in this repo
5. ffempg installed and in PATH

## What to run and how
1. Convert the file using AAXtoMP3 (select an aax downloaded to the machine). You should now have an MP3.
2. Run AudibleChapters and get a text file with the list of chapters. Don't attempt to run conversions, just the aax file as input, and put the output in a text file. You shoul have a text file that has the list of chapters. [Here is an example](https://github.com/guysoft/aax_to_mp3_splitter/blob/master/data_file_example.txt).
3. Create an empty folder
4. Run the program this script like this: `python3 splitter.py data_file_example.txt book.mp3 /tmp`

```
splitter.py [-h] file_name input_file output_dir

Split an mp3 encoded with AAX2MP3 based on an AAXchapters2.0 output file

positional arguments:
  file_name   The file data from AAX chapters 2.0
  input_file  The mp3 file
  output_dir  The output folder, should be created

optional arguments:
  -h, --help  show this help message and exit
```
