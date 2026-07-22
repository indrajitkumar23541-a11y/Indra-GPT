"""FastAPI app creation, logger configuration and main API routes."""


from indra_gpt.di import get_global_injector
from indra_gpt.launcher import create_app

app = create_app(get_global_injector())
