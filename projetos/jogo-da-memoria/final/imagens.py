"""Ajuste das imagens enviadas: todas viram PNG quadrado do mesmo tamanho."""

import uuid

from PIL import Image, ImageDraw, ImageOps, UnidentifiedImageError


def salvar_imagem(arquivo, pasta, tamanho):
    """Ajusta a imagem a tamanho x tamanho sem distorcer e salva como PNG.

    Devolve o nome do arquivo salvo, ou None se o arquivo não for uma imagem.
    """
    try:
        imagem = Image.open(arquivo)
        imagem = ImageOps.exif_transpose(imagem)  # foto de celular "deitada"
    except (UnidentifiedImageError, OSError):
        return None
    # pad: aumenta ou reduz até caber no quadrado e completa a sobra com transparente
    imagem = ImageOps.pad(imagem.convert("RGBA"), (tamanho, tamanho),
                          method=Image.Resampling.LANCZOS, color=(0, 0, 0, 0))
    nome = f"{uuid.uuid4().hex}.png"
    pasta.mkdir(parents=True, exist_ok=True)
    imagem.save(pasta / nome)
    return nome


def desenhar_formas(pasta, tamanho):
    """Gera as imagens do tema inicial: 4 formas em 3 cores."""
    cores = ["#ef476f", "#ffd166", "#06d6a0"]
    m, t = tamanho // 8, tamanho - tamanho // 8  # margem e limite
    meio = tamanho // 2
    formas = [
        lambda d, c: d.ellipse((m, m, t, t), fill=c),
        lambda d, c: d.rectangle((m, m, t, t), fill=c),
        lambda d, c: d.polygon([(meio, m), (t, t), (m, t)], fill=c),
        lambda d, c: d.polygon([(meio, m), (t, meio), (meio, t), (m, meio)], fill=c),
    ]
    nomes = []
    pasta.mkdir(parents=True, exist_ok=True)
    for desenhar in formas:
        for cor in cores:
            imagem = Image.new("RGBA", (tamanho, tamanho), (0, 0, 0, 0))
            desenhar(ImageDraw.Draw(imagem), cor)
            nome = f"{uuid.uuid4().hex}.png"
            imagem.save(pasta / nome)
            nomes.append(nome)
    return nomes
