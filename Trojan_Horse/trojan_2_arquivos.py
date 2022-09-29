import os, base64
archive_01 = input("Caminho do arquivo 1 (com extensão): ")
archive_02 = input("Caminho do arquivo 2 (com extensão): ")
archive01_name = os.path.basename(archive_01)
archive02_name = os.path.basename(archive_02)

with open(archive_01, 'rb') as a1_open:
    with open(archive_02, 'rb') as a2_open:
        with open('final_archive.py', 'w') as new_archive:
            new_archive.write('''import os, base64
            def join(binary_content, archive_name):
                if not os.path.exists(os.environ["TEMP"]+"\\\\"+archive_name):
                    with open(os.environ["TEMP"]+"\\\\"+archive_name, "wb") as temp_archive:
                              temp_archive.write(binary_content)
                os.startfile(os.environ["TEMP"]+"\\\\"+archive_name)
            archive01_base64 = "%s"
            join(base64.b64decode(archive01_base64), "%s")
            archive02_base64 = "%s"
            join(base64.b64decode(archive02_base64), "%S")
            '''%(base64.b64encode(a1_open.read()), archive01_name, base64.b64encode(a2_open.read()), archive02_name))

#Usar o pyinstaller para gerar um executável.