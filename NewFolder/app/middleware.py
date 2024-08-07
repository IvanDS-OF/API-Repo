import time 

from fastapi import  Request




async def add_process_time_header(request: Request, call_next): 

    start = time.time()
    response = await call_next(request)
    total_time = time.time() - start
    response.headers["X-Process-Time"] = str(total_time)
    return response



