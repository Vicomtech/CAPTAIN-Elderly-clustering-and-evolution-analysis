from pyngrok import ngrok


if __name__ == "__main__":
    # Setup a tunnel to the streamlit port 8501
    public_url = ngrok.connect(8501)
    print(f'Public URL: {public_url}')
    value = input('Press return to kill ngrok')
    # Destroy tunnel
    tunnels = ngrok.get_tunnels()
    for tunnel in tunnels:
        ngrok.disconnect(tunnel.public_url)
    ngrok.kill()
