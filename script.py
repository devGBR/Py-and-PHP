from pylovepdf.ilovepdf import ILovePdf
import sys

def compress_file(file: str):
    public_key = 'project_public_d02b21686a597e4cc835f57185de6205_GFJ4Jd1cd74b3d4a0c693c7387991de28c85d'
    ilovepdf = ILovePdf(public_key, verify_ssl=True) 
    task = ilovepdf.new_task('compress') 
    task.add_file(file) 
    task.download()

if __name__ == "__main__":
    # Parsing command line arguments entered by user
    file = sys.argv[1]
    compress_file(file)
