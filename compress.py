from PDFNetPython3 import PDFDoc, Optimizer, SDFDoc, PDFNet
import sys
import  os  

def compress_file(input_file: str):
    initial_size = os.path.getsize(input_file)
    try:
        # Initialize the library
        PDFNet.Initialize()
        doc = PDFDoc(input_file)
        # Reduce PDF size by removing redundant information and compressing data streams
        Optimizer.Optimize(doc)
        newfile = input_file.replace(".pdf", "_compressed.pdf")
        file_size = os.path.getsize(newfile)
        file = int(file_size)
        if file > 5000000:
            # Initialize the library
            PDFNet.Initialize()
            doc = PDFDoc(input_file)
              # Reduce PDF size by removing redundant information and compressing data streams
            Optimizer.Optimize(doc)
            newfile = input_file.replace(".pdf", "_compressed.pdf")
            file_size = os.path.getsize(newfile)
            file1 = int(file_size)
            if file1 > 5000000:
                # Initialize the library
                PDFNet.Initialize()
                doc = PDFDoc(input_file)
                    # Reduce PDF size by removing redundant information and compressing data streams
                Optimizer.Optimize(doc)
                newfile = input_file.replace(".pdf", "_compressed.pdf")
                file_size = os.path.getsize(newfile)
                file2 = int(file_size)
                if file2 > 5000000:
                    # Initialize the library
                    PDFNet.Initialize()
                    doc = PDFDoc(input_file)
                      # Reduce PDF size by removing redundant information and compressing data streams
                    Optimizer.Optimize(doc)
                    newfile = input_file.replace(".pdf", "_compressed.pdf")
                    file_size = os.path.getsize(newfile)
                    file3 = int(file_size)
                    if file3 > 5000000:
                        # Initialize the library
                        PDFNet.Initialize()
                        doc = PDFDoc(input_file)
                         # Reduce PDF size by removing redundant information and compressing data streams
                        Optimizer.Optimize(doc)
                        newfile = input_file.replace(".pdf", "_compressed.pdf")
                        file_size = os.path.getsize(newfile)
                        file4 = int(file_size)
                        if file4 > 5000000:
                            # Initialize the library
                            PDFNet.Initialize()
                            doc = PDFDoc(input_file)
                            # Reduce PDF size by removing redundant information and compressing data streams
                            Optimizer.Optimize(doc)
                            newfile = input_file.replace(".pdf", "_compressed.pdf")
                            file_size = os.path.getsize(newfile)
                            file5 = int(file_size)
                            if file5 > 5000000:
                                # Initialize the library
                                PDFNet.Initialize()
                                doc = PDFDoc(input_file)
                                # Reduce PDF size by removing redundant information and compressing data streams
                                Optimizer.Optimize(doc)
                                newfile = input_file.replace(".pdf", "_compressed.pdf")
                                file_size = os.path.getsize(newfile)
                                file6 = int(file_size)
                                if file6 > 5000000:
                                    # Initialize the library
                                    PDFNet.Initialize()
                                    doc = PDFDoc(input_file)
                                      # Reduce PDF size by removing redundant information and compressing data streams
                                    Optimizer.Optimize(doc)
                                    newfile = input_file.replace(".pdf", "_compressed.pdf")
                                    file_size = os.path.getsize(newfile)
                                    file7 = int(file_size)
                                    if file7 > 5000000:
                                        # Initialize the library
                                        PDFNet.Initialize()
                                        doc = PDFDoc(input_file)
                                          # Reduce PDF size by removing redundant information and compressing data streams
                                        Optimizer.Optimize(doc)
                                        newfile = input_file.replace(".pdf", "_compressed.pdf")
                                        file_size = os.path.getsize(newfile)
                                        file8 = int(file_size)
                                        if file8 < 5000000:
                                            doc.Save(newfile, SDFDoc.e_linearized)
                                            doc.Close()
                                            print("File compressed")
                                        else:
                                            print("failed is compression")
        else:
            print("failed is compression")
    except Exception as e:
        print("Error compress_file=", e)
        doc.Close()

    return newfile

if __name__ == "__main__":
    # Parsing command line arguments entered by user
    input_file = sys.argv[1]
    compress_file(input_file)