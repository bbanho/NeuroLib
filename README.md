Para executar a instalação automática basta copiar o conteúdo deste diretório para onde deseja instalar. A seguir, execute diretamente o script install.sh.

$ cd auto
$ sh install.sh

=============================================================

(Opcional) Também é possível conceder permissão de executável.

$ chmod +x install.sh
$ ./install.sh

(etc)
$ ./install.sh > log

O script se encarregará de realizar as instalações necessárias.

Para testar se a instalação ocorreu corretamente, fornecer as imagens e executar

python3 NeuroLib.py
python3 NeuroFrame.py
