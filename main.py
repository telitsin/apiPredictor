import uvicorn
import platform

# CURRENT_HOST = '0.0.0.0' # choose this if you need to use physical IP
CURRENT_HOST = '127.0.0.1'
"""Use http://127.0.0.1:3500/docs link to check the API"""

if __name__ == '__main__':
    uvicorn.run(
        "app:app",
        host=CURRENT_HOST,
        port=3500,  # modify port if necessary
        reload=True
    )

