from fastapi import FastAPI
from .routers import image_routes, doc_routes, video_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API de Conversão de Arquivos",
    description="Uma API para converter diversos tipos de arquivos entre múltiplos formatos (imagens, documentos, vídeos).",
    version="1.0.0"
)


origins = [
    "http://localhost:5173",  # Adicione a origem do front-end
    # Você pode adicionar outras origens, se necessário
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas referentes a cada tipo
app.include_router(image_routes.router, prefix="/images", tags=["images"])
app.include_router(doc_routes.router, prefix="/documents", tags=["documents"])
app.include_router(video_routes.router, prefix="/video", tags=["video"])

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Conversão de Arquivos!"}
