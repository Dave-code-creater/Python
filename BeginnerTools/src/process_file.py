from PyPDF2 import PdfFileReader
import csv
import pandas as pd
import pyaudio
import wave
import whisper
import pafy

class PDFHandler(object):
    def __init__(self, path):
        self.path = path
        self.pdf = PdfFileReader(open(path, 'rb'))
    
    def get_text(self):
        text = ""
        for page_num in range(self.pdf.getNumPages()):
            page = self.pdf.getPage(page_num)
            text += page.extract_text() or ''
        return text
    
    def get_metadata(self):
        info = self.pdf.getDocumentInfo()
        return {
            "title": info.get('/Title', ''),
            "author": info.get('/Author', ''),
            "subject": info.get('/Subject', ''),
            "keywords": info.get('/Keywords', ''),
            "producer": info.get('/Producer', ''),
            "creator": info.get('/Creator', ''),
            "creation_date": info.get('/CreationDate', ''),
            "modification_date": info.get('/ModDate', '')
        }
    
    def convert_to_text(self):
        with open(self.path.replace('.pdf', '.txt'), 'w') as file:
            file.write(self.get_text())

class CSVHandler(object):
    def __init__(self, path):
        self.path = path
        self.data = []
        with open(path, 'r') as file:
            reader = csv.reader(file)
            self.data = [row for row in reader]
    
    def get_data(self):
        return self.data
    
    def get_row(self, row_num):
        return self.data[row_num] if row_num < len(self.data) else []
    
    def get_column(self, col_num):
        return [row[col_num] for row in self.data if col_num < len(row)]
    
    def get_cell(self, row_num, col_num):
        return self.data[row_num][col_num] if row_num < len(self.data) and col_num < len(self.data[row_num]) else None
    
    def get_num_rows(self):
        return len(self.data)
    
    def get_num_columns(self):
        return len(self.data[0]) if self.data else 0
    
    def get_headers(self):
        return self.data[0] if self.data else []
    
    def convert_df(self):
        return pd.DataFrame(self.data[1:], columns=self.data[0])

class AudioHandler(object):
    def __init__(self, path):
        self.path = path
        self.audio = wave.open(path, 'rb')
        self.p = pyaudio.PyAudio()
        self.model = whisper.load_model("tiny")
    
    def record_audio(self, seconds, output_path):
        stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        frames = [stream.read(1024) for _ in range(0, int(44100/1024 * seconds))]
        stream.stop_stream()
        stream.close()
        self.p.terminate()
        with wave.open(output_path, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(frames))
        
    def transcript_audio(self):
        return whisper.transcribe(self.path)
    
    def get_audio_data(self):
        return self.audio.getparams()
    
    def get_audio_duration(self):
        return self.audio.getnframes() / self.audio.getframerate()
    
    def get_audio_channels(self):
        return self.audio.getnchannels()
    
    def get_audio_sample_width(self):
        return self.audio.getsampwidth()

class YouTubeHandler(object):
    def __init__(self, url):
        self.url = url
        self.video = pafy.new(url)
    
    def get_title(self):
        return self.video.title
    
    def get_author(self):
        return self.video.author
    
    def get_description(self):
        return self.video.description
    
    def get_duration(self):
        return self.video.duration
    
    def get_rating(self):
        return self.video.rating
    
    def get_view_count(self):
        return self.video.viewcount
    
    def get_likes(self):
        return self.video.likes
    
    def get_dislikes(self):
        return self.video.dislikes
    
    def get_best_audio(self):
        return self.video.getbestaudio()
    
    def get_best_video(self):
        return self.video.getbest()
    
    def download_audio(self, path):
        audio = self.get_best_audio()
        audio.download(path)
    
    def download_video(self, path):
        video = self.get_best_video()
        video.download(path)
    
    def download_subtitle(self, path):
        subtitle = self.video.getbestsubtitle()
        subtitle.download(path)
    
    def get_audio_stream(self):
        return self.get_best_audio().url
    
    def get_video_stream(self):
        return self.get_best_video().url
    
    def get_subtitle_stream(self):
        return self.video.getbestsubtitle().url
