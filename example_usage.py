from client import BrowserNativeWasmMicrocontainerNodeRuntimeClient

def main():
    client = BrowserNativeWasmMicrocontainerNodeRuntimeClient()
    res = client.boot_wasm_node_container({'dependencies': {'next': '^14.2.0', 'react': '^18.3.1'}})
    print('Wasm Microcontainer: ' + res['container_session_id'] + ' (Status: ' + res['container_status'] + ')')
    print('Boot Latency: ' + str(res['boot_latency_ms']) + 'ms | VFS Mounted: ' + str(res['virtual_file_system_mounted']))
    print('Proxy Port: :' + str(res['tcp_loopback_proxy_port']) + ' | Memory Pages: ' + str(res['wasm_memory_pages_allocated']))
    print('Live Preview: ' + res['live_preview_url'])

if __name__ == '__main__':
    main()
