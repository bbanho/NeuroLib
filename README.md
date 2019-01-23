# Instalação
Para executar a instalação automática basta copiar o conteúdo deste diretório para onde deseja instalar. A seguir, execute diretamente o script install.sh.

```bash
$ git clone https://github.com/bbanho/NeuroLib.git
$ cd NeuroLib/auto
$ yes | sh install.sh
```

Ou apenas

```bash
$ git clone https://github.com/bbanho/NeuroLib.git; cd NeuroLib/auto; yes | sh install.sh
```
## Opcional
Também é possível conceder permissão de executável.
```bash
$ chmod +x install.sh
$ ./install.sh
```
## Etc
```bash
$ ./install.sh > log
```
O script se encarregará de realizar as instalações necessárias.

Para testar se a instalação ocorreu corretamente, fornecer as imagens e executar
```bash
$ python3 NeuroLib.py
$ python3 NeuroFrame.py
```
### TODO

* Observar licença de software proprietário
	* https://www.baslerweb.com/en/service/pylon-eula/

