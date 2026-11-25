# Mission 7 — How computers communicate

## 1. Task / objective
Explain common network terms, run `ping` and `nslookup`, and describe how a website loads in six steps.

## 2. Work completed
- Made a network concepts table explaining eight common networking terms in my own words with practical examples.
- Ran a connectivity test using `ping` to see if my laptop could reach `example.com`.
- Ran a DNS lookup using `nslookup` to see the IP address behind `example.com`.
- Wrote down what connectivity tests and DNS lookups tell you, and explained the role DNS plays.
- Wrote a 6-step numbered explanation of what happens from typing a website address to seeing the page on your screen.

---

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A small network connecting computers and devices in a limited area like a home, school lab, or office. | My home Wi-Fi connecting my laptop, phone, and printer together. |
| **MAN (Metropolitan Area Network)** | A medium-sized network that covers a whole neighborhood, college campus, or city. | A university network that connects all the different college buildings and hostels across a campus. |
| **WAN (Wide Area Network)** | A huge network that covers large distances across cities, countries, or the whole world. | The Internet, which connects millions of devices all over the globe. |
| **DNS (Domain Name System)** | Like a contacts list or phonebook for the internet that turns website names into number IP addresses. | Translating `example.com` into the IP address `172.66.147.243`. |
| **Router** | A network box that connects different networks together and directs data to the right place. | The Wi-Fi router at home that takes internet data from the cable and sends it to my laptop. |
| **Protocol** | An agreed set of rules that computers follow so they can understand each other when sending data. | `HTTP` or `HTTPS` for web pages, or `TCP` for sending data reliably. |
| **Packet switching** | Splitting data into small chunks (called packets), sending them across the network, and putting them back together at the destination. | Watching a video online where the video data travels in thousands of small packets and plays smoothly. |
| **Client-server** | A system where one device (the client) asks for information, and another powerful computer (the server) provides it. | My laptop using a browser (client) to request a page from YouTube's computer (server). |

---

### Task 7.2 — Observe network information

#### 1. Connectivity Test (`ping`):
- **Command executed:** `ping -c 3 example.com`
- **What I saw in the terminal:**
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
- **What I saw in the terminal:**
  ```text
  Server:		8.8.8.8
  Address:	8.8.8.8#53

  Non-authoritative answer:
  Name:	example.com
  Address: 104.20.23.154
  Name:	example.com
  Address: 172.66.147.243
  ```

#### Questions answered:
- **What a connectivity test helps you check:**
  `ping` lets you check if your computer can actually reach a specific website or server over the internet. It tells you if data packets are getting lost (packet loss) and how many milliseconds it takes for the signal to go there and come back (latency/speed).
- **What information a DNS lookup displays:**
  `nslookup` shows the real IP address of a website. It shows which DNS server helped look it up (like Google's `8.8.8.8`) and lists the IP addresses (like `172.66.147.243`) that belong to that domain name.
- **The role of DNS when you enter a website name in a browser:**
  Computers and routers can't find websites using English names like `google.com`; they can only route traffic using number IP addresses. DNS acts as the translator. The moment you press Enter, DNS looks up the name and tells your browser the exact IP address to connect to.

---

### Task 7.3 — What happens when you open a website?

Here is what happens step by step when you open a website:

1. **Typing the URL:** You open your browser (the **client**) and type a website address like `https://example.com` into the search bar and press Enter.
2. **DNS Lookup:** Your browser needs to know where that website lives. It asks a **DNS** server to look up the domain name. The DNS server finds the matching IP address (like `172.66.147.243`) and sends it back to your computer.
3. **Connecting to the server:** Your browser uses network rules (the TCP and HTTPS **protocols**) to reach out to the **server** at that IP address and start a secure connection.
4. **Sending the request:** The browser sends an HTTP request asking the server to share the webpage files.
5. **Traveling through the network:** That request is chopped into small packets and sent through your home **router** and internet cables across the network using **packet switching** until it reaches the server.
6. **Receiving and displaying the page:** The **server** processes your request and sends back the webpage content in packets. Your browser catches the data, puts it together, and displays the page on your screen.

---

## 3. Commands / tools used
- `ping -c 3 example.com`: Tested internet connectivity, latency, and packet loss.
- `nslookup example.com`: Looked up the IP address connected to a domain name.

## 4. My understanding
Servers send website content to browsers over a network. `ping` checks reachability and response time, while `nslookup` shows DNS results. DNS lets me use names instead of remembering IP addresses.

## 5. Difficulties faced
`nslookup` returned two IP addresses for `example.com`, which surprised me.

## 6. How I resolved them
I learned that a domain can have multiple IP addresses to help distribute traffic and improve availability.

## 7. Evidence / files
- `mission-07-networking/README.md`: Networking concepts table, terminal outputs, and 6-step website explanation.

## 8. Commit details
- Commit message: `Explain networking concepts and website communication`
- Branch: `main`
- Remote URL: `https://github.com/Harshiita24/digital-detective-8020`
