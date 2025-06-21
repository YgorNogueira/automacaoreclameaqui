# README

## Descrição

Este script automatiza a coleta de reclamações do Reclame Aqui utilizando uma automação RPA desenvolvida com **PyAutoGUI** e **Pyperclip**.

## Pré-requisitos

* **Python 3.x** instalado.
* Bibliotecas Python:

  ```bash
  pip install pyautogui pyperclip
  ```

## Passo a passo para usar

1. **Clone ou baixe** este repositório na sua máquina.
2. **Instale** as dependências:

   ```bash
   pip install pyautogui pyperclip
   ```
3. **Execute** o script `ponto.py` para obter as coordenadas de referência (início do arraste, fim do arraste e posição do botão). Ele exibirá as posições atuais do mouse no console quando você clicar nos pontos desejados.
4. **Atualize** o arquivo principal (`autoguireclameaqui.py`) substituindo as variáveis de coordenadas pelos valores obtidos em `ponto.py`.
5. **Abra** o navegador na página de reclamações desejada (Reclame Aqui) e ajuste o zoom para **100%**.
6. **Execute** o script principal:

   ```bash
   python autoguireclameaqui.py
   ```
7. **Aguarde** a automação percorrer as páginas e coletar até 18 reclamações. As reclamações serão copiadas e adicionadas incrementalmente no arquivo `reclamacoes.txt`.

## Estrutura de arquivos

* `autoguireclameaqui.py` : Script principal que realiza o scroll, arraste, cópia e gravação das reclamações.
* `ponto.py`              : Script auxiliar para capturar coordenadas de referência na tela.
* `reclamacao.png`        : Template de imagem para encontrar o cabeçalho "Reclamações".
* `proxpag.png`           : Template de imagem para localizar o botão "Carregar mais".
* `reclamacoes.txt`       : Arquivo de saída onde as reclamações serão salvas.

## Observações

* **Tempos de espera** (`time.sleep`) podem precisar de ajustes de acordo com a velocidade da sua conexão e resposta do site.
* Caso **CAPTCHA** do Cloudflare apareça, resolva manualmente na janela do navegador antes que o script prossiga.
* Mantenha sempre o mesmo **zoom** e **tamanho** da janela do navegador para garantir que os templates de imagem sejam encontrados corretamente.
