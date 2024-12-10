def build_ffmpeg_command(input_path: str, output_path: str, extra_args: list) -> list:
    # Exemplo simples: retorna a lista de argumentos para o ffmpeg
    return ["ffmpeg", "-i", input_path] + extra_args + [output_path]
