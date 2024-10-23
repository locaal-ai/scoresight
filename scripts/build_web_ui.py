# build.py
import subprocess
import shutil
from pathlib import Path
import json
import os

def build_frontend():
    """Build the React frontend and move it to the static directory"""
    # Create frontend directory if it doesn't exist
    frontend_dir = Path(os.path.join(Path(__file__).parent, "frontend"))
    frontend_dir.mkdir(exist_ok=True)

    # Create package.json with additional shadcn/ui dependencies
    package_json = {
        "name": "scoresight-web",
        "version": "1.0.0",
        "private": True,
        "dependencies": {
            "react": "^18.2.0",
            "react-dom": "^18.2.0",
            "@vitejs/plugin-react": "^4.2.0",
            "vite": "^5.0.0",
            "lucide-react": "^0.263.1",
            "tailwindcss": "^3.3.0",
            "autoprefixer": "^10.4.0",
            "postcss": "^8.4.0",
            "class-variance-authority": "^0.7.0",
            "clsx": "^2.0.0",
            "tailwind-merge": "^2.0.0",
            "@radix-ui/react-tabs": "^1.0.4",
            "@radix-ui/react-slot": "^1.0.2"
        },
        "scripts": {
            "dev": "vite",
            "build": "vite build",
            "preview": "vite preview"
        }
    }
    
    with open(frontend_dir / "package.json", "w") as f:
        json.dump(package_json, f, indent=2)

    # Create components directory structure
    components_dir = frontend_dir / "src" / "components" / "ui"
    components_dir.mkdir(parents=True, exist_ok=True)

    # Create lib/utils.js
    lib_dir = frontend_dir / "src" / "lib"
    lib_dir.mkdir(parents=True, exist_ok=True)
    
    with open(lib_dir / "utils.js", "w") as f:
        f.write("""
import { clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs) {
  return twMerge(clsx(inputs))
}
        """.strip())

    # Create card component
    with open(components_dir / "card.jsx", "w") as f:
        f.write("""
import * as React from "react"
import { cn } from "@/lib/utils"

const Card = React.forwardRef(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("rounded-lg border bg-card text-card-foreground shadow-sm", className)}
    {...props}
  />
))
Card.displayName = "Card"

const CardHeader = React.forwardRef(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex flex-col space-y-1.5 p-6", className)}
    {...props}
  />
))
CardHeader.displayName = "CardHeader"

const CardTitle = React.forwardRef(({ className, ...props }, ref) => (
  <h3
    ref={ref}
    className={cn("text-2xl font-semibold leading-none tracking-tight", className)}
    {...props}
  />
))
CardTitle.displayName = "CardTitle"

const CardContent = React.forwardRef(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("p-6 pt-0", className)} {...props} />
))
CardContent.displayName = "CardContent"

export { Card, CardHeader, CardTitle, CardContent }
        """.strip())

    # Create tabs component
    with open(components_dir / "tabs.jsx", "w") as f:
        f.write("""
import * as React from "react"
import * as TabsPrimitive from "@radix-ui/react-tabs"
import { cn } from "@/lib/utils"

const Tabs = TabsPrimitive.Root

const TabsList = React.forwardRef(({ className, ...props }, ref) => (
  <TabsPrimitive.List
    ref={ref}
    className={cn(
      "inline-flex h-10 items-center justify-center rounded-md bg-muted p-1 text-muted-foreground",
      className
    )}
    {...props}
  />
))
TabsList.displayName = TabsPrimitive.List.displayName

const TabsTrigger = React.forwardRef(({ className, ...props }, ref) => (
  <TabsPrimitive.Trigger
    ref={ref}
    className={cn(
      "inline-flex items-center justify-center whitespace-nowrap rounded-sm px-3 py-1.5 text-sm font-medium ring-offset-background transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 data-[state=active]:bg-background data-[state=active]:text-foreground data-[state=active]:shadow-sm",
      className
    )}
    {...props}
  />
))
TabsTrigger.displayName = TabsPrimitive.Trigger.displayName

const TabsContent = React.forwardRef(({ className, ...props }, ref) => (
  <TabsPrimitive.Content
    ref={ref}
    className={cn(
      "mt-2 ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2",
      className
    )}
    {...props}
  />
))
TabsContent.displayName = TabsPrimitive.Content.displayName

export { Tabs, TabsList, TabsTrigger, TabsContent }
        """.strip())

    # Create vite.config.js with path alias
    with open(frontend_dir / "vite.config.js", "w") as f:
        f.write("""
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
})
        """.strip())

    # Create tailwind.config.js
    with open(frontend_dir / "tailwind.config.js", "w") as f:
        f.write("""
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  content: [
    './src/**/*.{js,jsx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
        """.strip())

    # Create postcss.config.js
    with open(frontend_dir / "postcss.config.js", "w") as f:
        f.write("""
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
        """.strip())

    # Copy React component to frontend/src
    src_dir = frontend_dir / "src"
    src_dir.mkdir(exist_ok=True)
    
    with open(src_dir / "App.jsx", "w") as f:
        f.write("""
import React from 'react';
import ScoreSight from './ScoreSight';

function App() {
    return <ScoreSight />;
}

export default App;
        """.strip())

    # Create index.html
    with open(frontend_dir / "index.html", "w") as f:
        f.write("""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>ScoreSight</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
        """.strip())

    # Create main.jsx
    with open(src_dir / "main.jsx", "w") as f:
        f.write("""
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
        """.strip())

    # Create index.css with Tailwind imports
    with open(src_dir / "index.css", "w") as f:
        f.write("""
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 224 71.4% 4.1%;
    --card: 0 0% 100%;
    --card-foreground: 224 71.4% 4.1%;
    --muted: 220 14.3% 95.9%;
    --muted-foreground: 220 8.9% 46.1%;
    --ring: 262.1 83.3% 57.8%;
  }
}
        """.strip())

    # Copy your ScoreSight component
    with open(src_dir / "ScoreSight.jsx", "w") as f:
        # Here we need to paste the ScoreSight component we created earlier
        # For brevity, I'm not including the full component here
        f.write("""// Your ScoreSight component code goes here""")

    # Install dependencies and build
    try:
        subprocess.run(["npm", "install"], cwd=frontend_dir, check=True)
        subprocess.run(["npm", "run", "build"], cwd=frontend_dir, check=True)

        # Move build files to static directory
        static_dir = Path("static")
        if static_dir.exists():
            shutil.rmtree(static_dir)
        shutil.copytree(frontend_dir / "dist", static_dir)
        
        print("Frontend built successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error building frontend: {e}")
        raise

if __name__ == "__main__":
    build_frontend()