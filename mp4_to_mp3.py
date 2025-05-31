from moviepy import VideoFileClip
import uuid

def mp4_to_mp3(mp4, mp3):
    try:
        video = VideoFileClip(mp4)
        audio = video.audio
        audio.write_audiofile(mp3)
        video.close()
        audio.close()

    except FileNotFoundError:
        print(f"Erro: O arquivo MP4 '{mp4}' não foi encontrado.")

    except Exception as e:
        print(f"Ocorreu um erro durante a conversão: {e}")



if __name__ == "__main__":
    mp4_local_filename = "entrevista_jo.mp4"
    mp3_local_filename = f"{uuid.uuid4().hex}.mp3"
    
    mp4_to_mp3(mp4_local_filename, mp3_local_filename)
