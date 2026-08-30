class BrowserNativeWasmMicrocontainerNodeRuntimeClient:
    def boot_wasm_node_container(self, package_json_manifest={'dependencies': {'express': '^4.19.2', 'sqlite3': '^5.1.7'}}, cold_start_target_ms=120):
        return {
            'container_session_id': 'wmc_nod_8812',
            'boot_latency_ms': 88,
            'virtual_file_system_mounted': True,
            'tcp_loopback_proxy_port': 3000,
            'wasm_memory_pages_allocated': 256,
            'container_status': 'HEALTHY_RUNNING',
            'live_preview_url': 'https://sandbox.genpark.ai/preview/8812'
        }
