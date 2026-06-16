import re

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error: {e}")
        return

    # 1. Shift the main group up to avoid overlapping with bottom text
    content = content.replace('<g transform="translate(640, 420)">', '<g transform="translate(640, 350)">')

    # 2. Fix the connection lines
    new_lines = r'''                    <!-- PERFECTLY JOINED CONNECTOR LINES -->
                    <g stroke="#E37322" stroke-width="1.5" fill="none">
                        
                        <!-- Line 1: From Browser wireframe to Orange Code Panel -->
                        <polyline points="-180,40 -120,0 -80,-30" stroke-dasharray="4 3" marker-end="url(#arrow-org-13)" />
                        <!-- Box A -->
                        <rect x="-140" y="10" width="16" height="16" fill="#F8F9FA" stroke="#E37322" />
                        <text x="-132" y="22" font-family="Arial, sans-serif" font-size="8" font-weight="bold" fill="#E37322" text-anchor="middle" stroke="none">A</text>

                        <!-- Line 2: From Orange Code Panel to Building Crane -->
                        <polyline points="-60,-70 20,-110 120,-150" stroke-dasharray="4 3" marker-end="url(#arrow-org-13)" />
                        <!-- Box REV -->
                        <rect x="10" y="-105" width="22" height="14" fill="#F8F9FA" stroke="#E37322" />
                        <text x="21" y="-95" font-family="Arial, sans-serif" font-size="7" font-weight="bold" fill="#E37322" text-anchor="middle" stroke="none">REV</text>

                        <!-- Line 3: From Browser to Building Base -->
                        <polyline points="-120,130 0,90 140,50" stroke-dasharray="4 3" marker-end="url(#arrow-org-13)" />
                        <!-- Box B -->
                        <rect x="-20" y="100" width="16" height="16" fill="#F8F9FA" stroke="#E37322" />
                        <text x="-12" y="112" font-family="Arial, sans-serif" font-size="8" font-weight="bold" fill="#E37322" text-anchor="middle" stroke="none">B</text>

                    </g>
                </g>
            </svg>'''

    pattern = r'                    <!-- PERFECTLY JOINED CONNECTOR LINES -->.*?</svg>'
    content = re.sub(pattern, new_lines, content, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Alignment and connection lines fixed.")

if __name__ == "__main__":
    main()
