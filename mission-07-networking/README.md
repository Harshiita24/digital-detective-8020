# Mission 7 — How computers communicate

## 1. Task / objective
The goal of Mission 7 is to understand the foundations of computer networking and web communications. This involves defining key network architectures (LAN, MAN, WAN), fundamental networking concepts (DNS, routers, protocols, packet switching, client-server models), conducting real connectivity and DNS resolution tests from the terminal (`ping` and `nslookup`), and detailing the step-by-step lifecycle of how a web browser requests, routes, and renders a webpage.

## 2. Work completed
- Built a network concepts reference table explaining eight foundational networking terms in my own words with everyday examples.
- Conducted live terminal network experiments using `ping` and `nslookup` against `example.com`, capturing real latency, packet transmission, and DNS resolver outputs.
- Documented answers to networking questions covering connectivity testing, DNS lookup data, and the role of DNS resolution during browsing.
- Formulated a clear, numbered 7-step guide explaining what happens behind the scenes from the moment a URL is entered into a browser to the point the page is fully rendered.

---

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A private computer network that covers a limited geographic radius, such as a home, a university computer lab, or a single office floor. | A home Wi-Fi network connecting a laptop, mobile phone, smart television, and wireless printer. |
| **MAN (Metropolitan Area Network)** | A high-speed network that covers a larger geographic region than a LAN, typically spanning an entire university campus, school district, or city. | A municipal fiber-optic network connecting civic offices, libraries, and public emergency services across a city. |
| **WAN (Wide Area Network)** | A telecommunications network spanning large geographical regions, linking cities, states, nations, or continents together. | The global public Internet, or an international commercial bank's network linking regional data centers globally. |
| **DNS (Domain Name System)** | The distributed directory of the internet that translates human-memorable domain names into machine-readable numerical IP addresses. | Resolving the domain name `example.com` into the destination IP address `172.66.147.243`. |
| **Router** | A specialized network device that inspects arriving data packets and directs them across different network boundaries toward their destination. | A home Wi-Fi gateway router forwarding outbound requests from your private home LAN to your ISP's wide-area network. |
| **Protocol** | A formal set of agreed-upon rules and communication conventions that devices follow so they can reliably understand and exchange data. | Hypertext Transfer Protocol Secure (`HTTPS`) for encrypted web traffic, or `TCP` for ordered, reliable packet delivery. |
| **Packet switching** | A communication method where digital messages are broken down into small, numbered packets that travel independently across the fastest paths and get reassembled at the destination. | Streaming a YouTube video or sending an email where data travels as thousands of independent IP packets and arrives assembled in correct order. |
| **Client-server** | A structural computing architecture where a user device (the client) requests resources or services, and a dedicated host system (the server) fulfills that request. | Google Chrome (the client browser) sending an HTTP request to an Apache or Nginx web server hosting webpage files. |

---

### Task 7.2 — Observe network information

#### 1. Connectivity Test (`ping`):
- **Command executed:** `ping -c 3 example.com`
- **Captured output (privacy-safe):**
  ```text
  PING example.com (172.66.147.243): 56 data bytes
  64 bytes from 172.66.147.243: icmp_seq=0 ttl=58 time=5.291 ms
  64 bytes from 172.66.147.243: icmp_seq=1 ttl=58 time=4.604 ms
  64 bytes from 172.66.147.243: icmp_seq=2 ttl=58 time=7.036 ms

  --- example.com ping statistics ---
  3 packets transmitted, 3 packets received, 0.0% packet loss
  round-trip min/avg/max/stddev = 4.604/5.644/7.036/1.024 ms
  ```

#### 2. DNS Lookup (`nslookup`):
- **Command executed:** `nslookup example.com`
- **Captured output (privacy-safe):**
  ```text
  Server:		8.8.8.8
  Address:	8.8.8.8#53

  Non-authoritative answer:
  Name:	example.com
  Address: 104.20.23.154
  Name:	example.com
  Address: 172.66.147.243
  ```

#### Network Questions:
- **What a connectivity test helps you check:**
  A connectivity tool like `ping` uses the Internet Control Message Protocol (ICMP) to verify if a remote computer is online and reachable across the network. It tells you whether network packets are actually making the journey without being dropped (packet loss percentage) and measures round-trip latency (how many milliseconds it takes for a signal to travel there and back).
- **What information a DNS lookup displays:**
  A DNS lookup displays the translation between a domain name and its underlying network addresses. It identifies which DNS resolver server answered the request (`8.8.8.8` on port 53), whether the response is authoritative, and lists the destination IPv4 or IPv6 addresses mapped to that domain (`104.20.23.154` and `172.66.147.243`).
- **Describe the role of DNS when you enter a website name in a browser:**
  Network hardware and routers cannot route data packets using English names like `google.com`; they only understand numerical binary and IP addresses. DNS acts as an automated lookup directory. When you enter a web address, your browser queries DNS first to discover the server's IP address. Once the IP is returned, the browser knows where on the internet to send its connection request.

---

### Task 7.3 — What happens when you open a website?

A step-by-step breakdown of how a web client communicates with a web server:

1. **User input at the client:** The user enters a website URL (e.g., `https://example.com`) into the browser's address bar and presses Enter. The browser acts as the **client**.
2. **DNS Resolution:** The browser checks its local cache. If the domain's IP is not cached, the client issues a query using the **DNS** protocol to a recursive resolver. The resolver queries root, TLD, and authoritative name servers until it returns the server's numerical IP address (`172.66.147.243`).
3. **Transport connection setup:** Using the TCP **protocol**, the client initiates a 3-way handshake (SYN, SYN-ACK, ACK) with the web server on port 443. For HTTPS, a cryptographic TLS handshake immediately follows to negotiate encryption keys.
4. **Sending the HTTP request:** Once the secure connection is open, the browser client generates an HTTP GET request message specifying the requested resource path, accepted formats, and browser headers.
5. **Packet routing across the network:** The operating system splits the request into digital packets. The local **router** inspects the IP headers and forwards the packets across intermediate ISP routers using **packet switching** until they reach the destination server.
6. **Server processing and response:** The destination **server** reassembles the incoming packets, reads the HTTP request, retrieves the requested file (HTML document, images, or stylesheets), and sends back an HTTP response containing a status code (e.g. `200 OK`) and the web page content.
7. **Rendering on the client:** The response packets travel back to the client machine. The browser parses the incoming HTML text, constructs the Document Object Model (DOM), loads associated CSS and JavaScript, and renders the visual website onto the monitor screen for the user.

---

## 3. Commands / tools used
- `ping -c 3 example.com`: Tested ICMP network reachability, packet loss, and latency metrics.
- `nslookup example.com`: Queried DNS servers to resolve domain names to public IPv4 addresses.
- Text editor: Documented findings, tables, and explanations.

## 4. My understanding
Networking is based on a layered set of cooperating rules. Before this mission, opening a website seemed like a single instant action. Walking through the steps showed that every web click triggers a rapid chain of events: a DNS lookup to find the numeric IP, a TCP/TLS handshake to establish an encrypted path, and packet switching across multiple routers before the server can even begin sending HTML data back. I also saw that protocols (like TCP, IP, DNS, and HTTPS) are what allow completely different computers made by different manufacturers to communicate without errors.

## 5. Difficulties faced
When looking at DNS outputs, it is common to see multiple IP addresses returned for a single domain name (such as `104.20.23.154` and `172.66.147.243` for `example.com`), which can be confusing if you assume one domain maps to only one computer.

## 6. How I resolved them
I learned that high-traffic websites use Content Delivery Networks (CDNs) and Anycast load balancers with multiple redundant server IP addresses. Having multiple IPs allows traffic to be distributed efficiently and ensures that if one server goes down, another can handle the traffic seamlessly.

## 7. Evidence / files
- `mission-07-networking/README.md`: Completed network concepts table, terminal test outputs, DNS questions, and the 7-step website communication lifecycle.

## 8. Commit details
- **Commit message:** `Explain networking concepts and website communication`
- **Target branch:** `main`
- **Remote destination:** `https://github.com/Harshiita24/digital-detective-8020`
