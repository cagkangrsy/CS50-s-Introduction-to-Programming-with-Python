input_string = input("Enter your file name as xxx.yy: ")
extension = input_string.split('.')[-1].lower().strip()
if extension in ["gif", "jpg", "jpeg", "png"]:
    if extension == "jpg":
        extension = "jpeg"
    print("image/" + extension)
elif extension in ["pdf", "zip"]:
    print("application/" + extension)
elif extension == "txt":
    print("text/plain")
else:
    print("application/octet-stream")
