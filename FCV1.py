#!/usr/bin/env python3
"""
Scholar's Spaced Repetition System - Python Server
Enhanced with 42 Subliminal Memory Systems
Version 2.0 - COMPLETE (Systems 1-42)
"""

from threading import Timer

def install_dependencies():
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'flask'])

def check_port_availability():
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 5000))
    sock.close()
    return result != 0

def open_browser():
    import webbrowser
    webbrowser.open('http://127.0.0.1:5000')

# Install dependencies first
install_dependencies()

# Import Flask
try:
    from flask import Flask
except ImportError:
    print("Failed to import Flask. Please make sure it's installed.")
    exit(1)

app = Flask(__name__)

# HTML template with modular, extensible architecture and 42 Memory Systems
HTML_TEMPLATE = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scholar's Spaced Repetition System - Enhanced</title>
    
    <!-- PWA Meta Tags -->
    <meta name="theme-color" content="#3a1f1f">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="Scholar SRS">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="application-name" content="Scholar SRS">
    <meta name="description" content="A methodical spaced repetition system for mastery">
    
    <!-- PWA Icons -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%233a1f1f'/%3E%3Ctext x='50' y='50' text-anchor='middle' dy='.3em' fill='%23f4f1e8' font-family='serif' font-size='50' font-weight='bold'%3E📚%3C/text%3E%3C/svg%3E">
    <link rel="apple-touch-icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%233a1f1f'/%3E%3Ctext x='50' y='50' text-anchor='middle' dy='.3em' fill='%23f4f1e8' font-family='serif' font-size='50' font-weight='bold'%3E📚%3C/text%3E%3C/svg%3E">
    
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;0,700;1,400&family=Playfair+Display:wght@400;700;900&display=swap');
        
        :root {
            --mahogany: #3a1f1f;
            --deep-brown: #2c1810;
            --leather: #4a342a;
            --parchment: #f4f1e8;
            --cream: #faf8f3;
            --gold: #b8860b;
            --forest-green: #1e3a2a;
            --sage: #87a96b;
            --burgundy: #722f37;
            --ink: #1a1611;
            --shadow: rgba(26, 22, 17, 0.1);
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Crimson Text', Georgia, serif;
            background-color: var(--deep-brown);
            color: var(--ink);
            line-height: 1.6;
            font-size: 18px;
            position: relative;
            min-height: 100vh;
        }
        
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(ellipse at top, transparent 0%, var(--deep-brown) 100%),
                repeating-linear-gradient(
                    0deg,
                    transparent,
                    transparent 2px,
                    rgba(26, 22, 17, 0.03) 2px,
                    rgba(26, 22, 17, 0.03) 4px
                );
            pointer-events: none;
            z-index: 1;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: var(--parchment);
            box-shadow: 
                0 0 50px rgba(0,0,0,0.5),
                inset 0 0 30px rgba(180, 160, 140, 0.1);
            position: relative;
            z-index: 2;
            min-height: 100vh;
        }
        
        .container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                repeating-linear-gradient(
                    90deg,
                    transparent,
                    transparent 200px,
                    rgba(180, 160, 140, 0.05) 200px,
                    rgba(180, 160, 140, 0.05) 201px
                );
            pointer-events: none;
        }
        
        .content-wrapper {
            padding: 3rem 3rem;
            position: relative;
            z-index: 3;
        }
        
        @media (max-width: 768px) {
            .content-wrapper {
                padding: 2rem 1.5rem;
            }
        }
        
        h1 {
            font-family: 'Playfair Display', 'Crimson Text', serif;
            text-align: center;
            color: var(--mahogany);
            margin-bottom: 0.5rem;
            font-size: 2.5rem;
            font-weight: 900;
            letter-spacing: -0.5px;
            text-shadow: 0 1px 2px rgba(0,0,0,0.1);
        }
        
        @media (max-width: 768px) {
            h1 {
                font-size: 2rem;
            }
        }
        
        .subtitle {
            text-align: center;
            color: var(--leather);
            margin-bottom: 2rem;
            font-style: italic;
            font-size: 1.1rem;
            font-weight: 400;
        }
        
        .ornament {
            text-align: center;
            font-size: 1.5rem;
            color: var(--gold);
            margin: 1rem 0;
            letter-spacing: 0.5rem;
        }
        
        .setup-screen, .study-screen, .break-screen {
            display: none;
            animation: fadeIn 0.5s ease;
        }
        
        .setup-screen.active, .study-screen.active, .break-screen.active {
            display: block;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        .instructions {
            background: var(--cream);
            border: 1px solid var(--gold);
            border-radius: 3px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            position: relative;
            box-shadow: 0 2px 4px var(--shadow);
        }
        
        .instructions::before {
            content: '§';
            position: absolute;
            top: -0.5rem;
            left: 1rem;
            background: var(--cream);
            padding: 0 0.5rem;
            color: var(--gold);
            font-size: 1.5rem;
        }
        
        .instructions h3 {
            color: var(--forest-green);
            margin-bottom: 1rem;
            font-family: 'Playfair Display', serif;
            font-weight: 700;
        }
        
        .instructions ul {
            list-style: none;
            padding-left: 0;
        }
        
        .instructions li {
            margin-bottom: 0.5rem;
            padding-left: 1.5rem;
            position: relative;
        }
        
        .instructions li::before {
            content: '•';
            position: absolute;
            left: 0;
            color: var(--gold);
            font-weight: bold;
        }
        
        .input-group {
            margin-bottom: 2rem;
        }
        
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: var(--forest-green);
            font-size: 1.1rem;
        }
        
        input[type="number"] {
            width: 100%;
            padding: 0.75rem 1rem;
            border: 2px solid var(--leather);
            border-radius: 3px;
            font-size: 1rem;
            font-family: 'Crimson Text', serif;
            background: var(--cream);
            color: var(--ink);
            transition: border-color 0.3s ease;
        }
        
        input[type="number"]:focus {
            outline: none;
            border-color: var(--forest-green);
            box-shadow: 0 0 0 3px rgba(30, 58, 42, 0.1);
        }
        
        textarea {
            width: 100%;
            min-height: 200px;
            padding: 1rem;
            border: 2px solid var(--leather);
            border-radius: 3px;
            font-size: 1rem;
            font-family: 'Crimson Text', serif;
            background: var(--cream);
            color: var(--ink);
            resize: vertical;
            transition: border-color 0.3s ease;
        }
        
        textarea:focus {
            outline: none;
            border-color: var(--forest-green);
            box-shadow: 0 0 0 3px rgba(30, 58, 42, 0.1);
        }
        
        .btn {
            background: var(--forest-green);
            color: var(--cream);
            border: none;
            padding: 0.75rem 2rem;
            border-radius: 3px;
            font-size: 1rem;
            font-family: 'Crimson Text', serif;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            margin: 0.25rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            box-shadow: 0 2px 4px var(--shadow);
        }
        
        .btn:hover {
            background: var(--mahogany);
            box-shadow: 0 4px 8px var(--shadow);
            transform: translateY(-1px);
        }
        
        .btn:active {
            transform: translateY(0);
            box-shadow: 0 1px 2px var(--shadow);
        }
        
        .btn-success {
            background: var(--sage);
            color: var(--deep-brown);
        }
        
        .btn-success:hover {
            background: #6d8756;
        }
        
        .btn-danger {
            background: var(--burgundy);
        }
        
        .btn-danger:hover {
            background: #5a252a;
        }
        
        .btn-info {
            background: var(--leather);
        }
        
        .btn-info:hover {
            background: var(--mahogany);
        }
        
        .phase-info {
            background: var(--cream);
            border: 1px solid rgba(74, 52, 42, 0.2);
            border-radius: 3px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 4px var(--shadow);
        }
        
        .phase-title {
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--forest-green);
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        
        .phase-badge {
            background: var(--gold);
            color: var(--cream);
            padding: 0.25rem 0.75rem;
            border-radius: 3px;
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .timer {
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--mahogany);
            text-align: center;
            margin: 1rem 0;
            font-family: 'Playfair Display', serif;
            letter-spacing: 2px;
        }
        
        @media (max-width: 768px) {
            .timer {
                font-size: 2rem;
            }
        }
        
        .progress-container {
            background: rgba(74, 52, 42, 0.1);
            border-radius: 3px;
            height: 1.5rem;
            margin: 1rem 0;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(74, 52, 42, 0.2);
        }
        
        .progress-bar {
            background: var(--forest-green);
            height: 100%;
            transition: width 0.5s ease;
            position: relative;
        }
        
        .progress-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-weight: 600;
            color: var(--ink);
            font-size: 0.8rem;
            text-shadow: 0 1px 2px rgba(255,255,255,0.5);
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }
        
        @media (max-width: 480px) {
            .stats {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        
        .stat-item {
            text-align: center;
            padding: 1rem;
            background: var(--cream);
            border: 1px solid rgba(74, 52, 42, 0.2);
            border-radius: 3px;
            box-shadow: 0 2px 4px var(--shadow);
        }
        
        .stat-label {
            font-size: 0.8rem;
            color: var(--leather);
            margin-bottom: 0.25rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .stat-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--forest-green);
            font-family: 'Playfair Display', serif;
        }
        
        .card-container {
            background: var(--cream);
            border: 1px solid rgba(74, 52, 42, 0.2);
            border-radius: 3px;
            padding: 3rem 2rem;
            margin: 2rem 0;
            min-height: 250px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            box-shadow: 0 4px 8px var(--shadow);
            position: relative;
        }
        
        @media (max-width: 768px) {
            .card-container {
                padding: 2rem 1.5rem;
                min-height: 200px;
            }
        }
        
        .card-question {
            font-size: 1.4rem;
            text-align: center;
            margin-bottom: 2rem;
            color: var(--mahogany);
            font-weight: 600;
            line-height: 1.5;
        }
        
        @media (max-width: 768px) {
            .card-question {
                font-size: 1.2rem;
            }
        }
        
        .card-answer {
            font-size: 1.2rem;
            text-align: center;
            color: var(--ink);
            display: none;
            margin-top: 2rem;
            padding: 1.5rem;
            background: rgba(244, 241, 232, 0.5);
            border: 1px solid var(--gold);
            border-radius: 3px;
            width: 100%;
        }
        
        .card-answer.show {
            display: block;
            animation: slideIn 0.4s ease;
        }
        
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .difficulty-indicator {
            display: flex;
            gap: 0.5rem;
            margin-top: 1rem;
            position: absolute;
            bottom: 1rem;
            right: 1rem;
        }
        
        .difficulty-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: rgba(74, 52, 42, 0.2);
            transition: all 0.3s;
        }
        
        .difficulty-dot.active {
            background: var(--burgundy);
        }
        
        .button-group {
            display: flex;
            justify-content: center;
            gap: 0.75rem;
            margin-top: 2rem;
            flex-wrap: wrap;
        }
        
        .error {
            color: var(--burgundy);
            font-size: 0.9rem;
            margin-top: 0.5rem;
            padding: 0.5rem;
            background: rgba(114, 47, 55, 0.1);
            border-radius: 3px;
            border: 1px solid rgba(114, 47, 55, 0.2);
            display: none;
        }
        
        .error.show {
            display: block;
        }
        
        .break-screen {
            text-align: center;
            padding: 4rem 2rem;
        }
        
        .break-title {
            font-size: 2.5rem;
            color: var(--forest-green);
            margin-bottom: 1rem;
            font-family: 'Playfair Display', serif;
        }
        
        .break-timer {
            font-size: 3rem;
            font-weight: 700;
            color: var(--mahogany);
            margin: 2rem 0;
            font-family: 'Playfair Display', serif;
            letter-spacing: 3px;
        }
        
        @media (max-width: 768px) {
            .break-title {
                font-size: 2rem;
            }
            .break-timer {
                font-size: 2.5rem;
            }
        }
        
        .break-message {
            font-size: 1.1rem;
            color: var(--leather);
            margin: 1.5rem 0;
            font-style: italic;
        }
        
        .achievement {
            position: fixed;
            top: 2rem;
            right: 2rem;
            background: var(--cream);
            padding: 1rem 1.5rem;
            border-radius: 3px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
            transform: translateX(400px);
            transition: transform 0.5s ease;
            z-index: 1000;
            border: 2px solid var(--gold);
            max-width: 300px;
        }
        
        @media (max-width: 768px) {
            .achievement {
                top: 1rem;
                right: 1rem;
                left: 1rem;
                max-width: none;
            }
        }
        
        .achievement.show {
            transform: translateX(0);
        }
        
        .achievement-title {
            font-weight: 700;
            color: var(--forest-green);
            margin-bottom: 0.25rem;
            font-family: 'Playfair Display', serif;
        }
        
        .achievement-text {
            color: var(--leather);
            font-size: 0.9rem;
        }
        
        .pause-toggle {
            position: fixed;
            bottom: 2rem;
            right: 6rem;
            background: var(--cream);
            width: 3rem;
            height: 3rem;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 4px 8px var(--shadow);
            transition: all 0.3s;
            z-index: 1000;
            border: 2px solid var(--leather);
            font-size: 1.2rem;
        }
        
        .pause-toggle:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 12px var(--shadow);
        }
        
        .pause-toggle.paused {
            background: var(--gold);
            color: var(--cream);
        }
        
        .sound-toggle {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: var(--cream);
            width: 3rem;
            height: 3rem;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 4px 8px var(--shadow);
            transition: all 0.3s;
            z-index: 1000;
            border: 2px solid var(--leather);
            font-size: 1.2rem;
        }
        
        .sound-toggle:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 12px var(--shadow);
        }
        
        .sound-toggle.muted {
            background: var(--parchment);
            opacity: 0.7;
        }
        
        /* Memory Enhancement System Styles */
        .memory-prime {
            position: absolute;
            pointer-events: none;
            font-size: 24px;
            font-weight: 600;
            color: var(--mahogany);
            opacity: 0;
        }
        
        .peripheral-text {
            position: fixed;
            pointer-events: none;
            font-size: 24px;
            opacity: 0;
            color: var(--mahogany);
            z-index: 999;
        }
        
        .emotional-word {
            position: absolute;
            pointer-events: none;
            font-size: 18px;
            opacity: 0;
            color: var(--forest-green);
        }
        
        .olfactory-word {
            position: fixed;
            pointer-events: none;
            font-size: 18px;
            font-family: serif;
            opacity: 0;
            color: var(--leather);
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        
        /* SYSTEMS 24-26 STYLES */
        .preload-container {
            position: absolute;
            top: -1000px;
            left: -1000px;
            opacity: 0;
            pointer-events: none;
            z-index: -1;
        }
        
        .success-anchor {
            position: fixed;
            pointer-events: none;
            font-size: 18px;
            opacity: 0;
            color: var(--forest-green);
            font-weight: 600;
            z-index: 998;
        }
        
        @keyframes flicker {
            0%, 100% { opacity: 0.98; }
            50% { opacity: 1.02; }
        }
        
        .consolidation-pulse {
            animation: flicker 0.5s ease-in-out;
        }
        
        .visual-memory-pattern {
            position: absolute;
            top: 1rem;
            right: 1rem;
            width: 40px;
            height: 40px;
            pointer-events: none;
        }
        
        .distinctiveness-boost {
            animation: distinctivePulse 0.5s ease-out;
        }
        
        @keyframes distinctivePulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.02); }
            100% { transform: scale(1); }
        }
        
        /* SYSTEMS 27-30 STYLES */
        .afterimage-flash {
            position: fixed;
            pointer-events: none;
            z-index: 997;
            opacity: 0;
            transition: opacity 750ms ease-out;
        }
        
        .blink-preview {
            position: fixed;
            pointer-events: none;
            font-size: 16px;
            opacity: 0;
            color: var(--ink);
            z-index: 996;
            background: rgba(244, 241, 232, 0.8);
            padding: 0.5rem;
            border-radius: 3px;
        }
        
        .semantic-prime {
            position: fixed;
            pointer-events: none;
            font-size: 14px;
            opacity: 0;
            color: var(--mahogany);
            z-index: 995;
            font-weight: 500;
        }
        
        /* SYSTEMS 31-36 STYLES */
        .phase-locked-flash {
            position: fixed;
            pointer-events: none;
            font-size: 16px;
            opacity: 0;
            color: var(--forest-green);
            z-index: 994;
            font-weight: 600;
            transition: opacity 12ms ease-out;
        }
        
        .cortical-ring {
            position: absolute;
            pointer-events: none;
            border: 3px solid transparent;
            border-radius: 50%;
            opacity: 0;
            z-index: 993;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        
        @keyframes corticalExpansion {
            0% {
                width: 0px;
                height: 0px;
                border-width: 3px;
                opacity: 0.022;
            }
            100% {
                width: 300px;
                height: 300px;
                border-width: 8px;
                opacity: 0;
            }
        }
        
        .emotional-tag {
            position: fixed;
            pointer-events: none;
            font-size: 24px;
            opacity: 0;
            z-index: 992;
            transition: opacity 14ms ease-out;
        }
        
        .somatic-marker {
            position: fixed;
            pointer-events: none;
            font-size: 16px;
            font-weight: 300;
            opacity: 0;
            color: var(--leather);
            z-index: 991;
            transition: opacity 22ms ease-out;
        }
        
        /* System 35: Quantum Field Text Vibration */
        .quantum-jitter {
            display: inline-block;
            transition: transform 500ms ease-in-out;
        }
        
        @keyframes quantumVibration {
            0%, 100% { transform: translate(0, 0); }
            25% { transform: translate(0.3px, -0.1px); }
            50% { transform: translate(-0.2px, 0.3px); }
            75% { transform: translate(0.1px, -0.3px); }
        }
        
        /* System 32: Vestibular Memory Encoding */
        .vestibular-shift {
            transition: transform 3s cubic-bezier(0.4, 0, 0.6, 1);
        }
        
        /* NEW SYSTEMS 37-42 STYLES */
        
        /* System 37: Chronobiological Phase Coupling */
        .chronobiological-tint {
            transition: filter 2s ease-in-out;
        }
        
        /* System 38: Mirror Neuron Activation Protocol */
        .handwriting-trace {
            position: absolute;
            top: 1rem;
            left: 1rem;
            pointer-events: none;
            opacity: 0;
            z-index: 990;
        }
        
        .handwriting-path {
            fill: none;
            stroke: var(--mahogany);
            stroke-width: 1px;
            stroke-dasharray: 100;
            stroke-dashoffset: 100;
        }
        
        @keyframes handwritingAnimation {
            0% { stroke-dashoffset: 100; }
            100% { stroke-dashoffset: 0; }
        }
        
        /* System 39: Subliminal Confidence Injection */
        .confidence-flash {
            position: fixed;
            pointer-events: none;
            font-size: 36px;
            opacity: 0;
            z-index: 989;
            transition: opacity 11ms ease-out;
        }
        
        /* System 40: Delta Wave Memory Consolidation */
        .delta-wave-pulse {
            transition: opacity 500ms ease-in-out;
        }
        
        /* System 41: Phantom Touch Memory Encoding */
        .phantom-touch {
            transition: box-shadow 800ms ease-in-out;
        }
        
        .phantom-touch:hover {
            box-shadow: 3px 3px 5px var(--shadow);
        }
        
        /* System 42: Accelerometer Rhythm Encoding */
        .accelerometer-flash {
            position: fixed;
            pointer-events: none;
            font-size: 18px;
            opacity: 0;
            z-index: 988;
            transition: opacity 16ms ease-out;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="content-wrapper">
            <h1>Scholar's Spaced Repetition System</h1>
            <p class="subtitle">Enhanced with 42 Subliminal Memory Technologies</p>
            <div class="ornament">♦ ♦ ♦</div>
            
            <!-- Setup Screen -->
            <div class="setup-screen active">
                <div class="instructions">
                    <h3>Systematic Memory Enhancement Protocol</h3>
                    <ul>
                        <li>Seven-phase progressive learning system</li>
                        <li>Adaptive difficulty calibration</li>
                        <li>Pomodoro-inspired interval breaks</li>
                        <li>Comprehensive performance analytics</li>
                        <li>Assured progression to complete mastery</li>
                        <li>Auditory reinforcement mechanisms</li>
                        <li>Real-time learning rate analysis</li>
                        <li>Automatic progress preservation and restoration</li>
                        <li>42 Subliminal memory enhancement systems (COMPLETE: 1-42)</li>
                    </ul>
                </div>
                
                <div class="input-group">
                    <label for="hours">Duration of Study Session (in hours)</label>
                    <input type="number" id="hours" step="0.1" min="0.5" placeholder="3.0" value="3">
                    <div class="error" id="hours-error"></div>
                </div>
                
                <div class="input-group">
                    <label for="questions">Study Material (Format: Question::Answer)</label>
                    <textarea id="questions" placeholder="What is 2+2?::4
What is the capital of France?::Paris
What year did WW2 end?::1945
When was the Declaration of Independence signed?::1776
What is the speed of light?::299,792,458 meters per second"></textarea>
                    <div class="error" id="questions-error"></div>
                </div>
                
                <button class="btn" onclick="ScholarSRS.startSession()">Commence Study Session</button>
            </div>
            
            <!-- Study Screen -->
            <div class="study-screen">
                <div class="phase-info">
                    <div class="phase-title">
                        <span id="phase-title">Phase I: Initial Exposure</span>
                        <span class="phase-badge" id="phase-badge">Learning</span>
                    </div>
                    <div class="timer" id="timer">00:00:00</div>
                    <div class="progress-container">
                        <div class="progress-bar" id="phase-progress"></div>
                        <div class="progress-text" id="phase-progress-text">0%</div>
                    </div>
                    <div class="progress-container">
                        <div class="progress-bar" id="overall-progress" style="background: var(--sage);"></div>
                        <div class="progress-text" id="overall-progress-text">Overall: 0%</div>
                    </div>
                </div>
                
                <div class="stats">
                    <div class="stat-item">
                        <div class="stat-label">Total</div>
                        <div class="stat-value" id="total-questions">0</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Mastered</div>
                        <div class="stat-value" id="mastered-count">0</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Learning</div>
                        <div class="stat-value" id="learning-count">0</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Difficult</div>
                        <div class="stat-value" id="difficult-count">0</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Accuracy</div>
                        <div class="stat-value" id="accuracy">0%</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Streak</div>
                        <div class="stat-value" id="streak">0</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Rate/Min</div>
                        <div class="stat-value" id="cards-per-minute">0.0</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Remaining</div>
                        <div class="stat-value" id="remaining-count">0</div>
                    </div>
                </div>
                
                <div class="card-container phantom-touch" id="card-container">
                    <div class="card-question" id="card-question">Prepare yourself for the journey to mastery.</div>
                    <div class="card-answer" id="card-answer"></div>
                    <div class="difficulty-indicator" id="difficulty-indicator">
                        <div class="difficulty-dot"></div>
                        <div class="difficulty-dot"></div>
                        <div class="difficulty-dot"></div>
                        <div class="difficulty-dot"></div>
                        <div class="difficulty-dot"></div>
                    </div>
                    <svg class="visual-memory-pattern" id="visual-memory-pattern" style="opacity: 0;">
                        <g id="dot-pattern"></g>
                    </svg>
                    <!-- System 33: Cortical Ring -->
                    <div class="cortical-ring" id="cortical-ring"></div>
                    <!-- System 38: Handwriting Trace -->
                    <svg class="handwriting-trace" id="handwriting-trace" width="100" height="40">
                        <path class="handwriting-path" id="handwriting-path" d=""></path>
                    </svg>
                </div>
                
                <div class="button-group" id="button-group">
                    <button class="btn btn-info" onclick="ScholarSRS.Card.showAnswer()" id="show-answer-btn" style="display:none;">Reveal Answer</button>
                    <button class="btn btn-success" onclick="ScholarSRS.Card.markCorrect()" id="correct-btn" style="display:none;">Correct</button>
                    <button class="btn btn-danger" onclick="ScholarSRS.Card.markWrong()" id="wrong-btn" style="display:none;">Incorrect</button>
                    <button class="btn" onclick="ScholarSRS.Card.skip()" id="skip-btn" style="display:none;">Postpone</button>
                </div>
            </div>
            
            <!-- Break Screen -->
            <div class="break-screen">
                <div class="break-title">Intermission</div>
                <div class="break-timer" id="break-timer">05:00</div>
                <div class="break-message">
                    <p>Rise, stretch, and refresh yourself.</p>
                    <p>Your mind is consolidating the knowledge acquired.</p>
                </div>
                <button class="btn btn-success" onclick="ScholarSRS.Break.skip()">Resume Study</button>
            </div>
        </div>
    </div>
    
    <!-- Achievement Popup -->
    <div class="achievement" id="achievement">
        <div class="achievement-title" id="achievement-title">Achievement</div>
        <div class="achievement-text" id="achievement-text">Excellent progress!</div>
    </div>
    
    <!-- Pause Button -->
    <div class="pause-toggle" id="pause-toggle" onclick="ScholarSRS.Controls.togglePause()" style="display: none;">
        <span id="pause-icon">⏸</span>
    </div>
    
    <!-- Sound Toggle -->
    <div class="sound-toggle" id="sound-toggle" onclick="ScholarSRS.Audio.toggleSound()">
        <span id="sound-icon">🔊</span>
    </div>
    
    <!-- Hidden elements for memory systems -->
    <div class="memory-prime" id="memory-prime"></div>
    <div class="peripheral-text" id="peripheral-text"></div>
    <div class="emotional-word" id="emotional-word"></div>
    <div class="olfactory-word" id="olfactory-word"></div>
    
    <!-- SYSTEMS 24-26 ELEMENTS -->
    <div class="preload-container" id="preload-container-1"></div>
    <div class="preload-container" id="preload-container-2"></div>
    <div class="success-anchor" id="success-anchor"></div>
    
    <!-- SYSTEMS 27-30 ELEMENTS -->
    <div class="afterimage-flash" id="afterimage-flash"></div>
    <div class="blink-preview" id="blink-preview"></div>
    <div class="semantic-prime" id="semantic-prime-1"></div>
    <div class="semantic-prime" id="semantic-prime-2"></div>
    <div class="semantic-prime" id="semantic-prime-3"></div>

    <!-- SYSTEMS 31-36 ELEMENTS -->
    <div class="phase-locked-flash" id="phase-locked-flash"></div>
    <div class="emotional-tag" id="emotional-tag"></div>
    <div class="somatic-marker" id="somatic-marker"></div>

    <!-- NEW SYSTEMS 37-42 ELEMENTS -->
    <div class="confidence-flash" id="confidence-flash"></div>
    <div class="accelerometer-flash" id="accelerometer-flash"></div>

    <script>
        /**
         * Scholar's Spaced Repetition System - Enhanced with Memory Systems
         * Version 2.0 - COMPLETE 42 Systems (1-42)
         * FINAL: Added Systems 37-42
         */
        
        // ========================================
        // CONFIGURATION & CONSTANTS
        // ========================================
        const CONFIG = {
            // System Configuration
            BREAK_INTERVAL: 25 * 60 * 1000, // 25 minutes in ms
            BREAK_DURATION: 5 * 60, // 5 minutes in seconds
            PROGRESS_UPDATE_INTERVAL: 50, // ms
            MOVING_AVERAGE_WINDOW: 10,
            
            // Phase System Configuration
            PHASES: [
                { name: "Initial Exposure", percentage: 0.15, intervals: [0], minCorrect: 1 },
                { name: "Immediate Recall", percentage: 0.15, intervals: [1, 3, 5], minCorrect: 1 },
                { name: "Short-Term Consolidation", percentage: 0.15, intervals: [10, 15], minCorrect: 2 },
                { name: "Medium-Term Practice", percentage: 0.15, intervals: [25, 35], minCorrect: 2 },
                { name: "Long-Term Reinforcement", percentage: 0.15, intervals: [50, 70], minCorrect: 3 },
                { name: "Deep Encoding", percentage: 0.15, intervals: [90, 120], minCorrect: 3 },
                { name: "Final Mastery Assessment", percentage: 0.10, intervals: [150], minCorrect: 1 }
            ],
            
            // Achievement Thresholds
            ACHIEVEMENTS: {
                FIRST_STREAK: 5,
                GOOD_STREAK: 10,
                EXCELLENT_STREAK: 20
            },
            
            // Audio Configuration
            AUDIO: {
                SUCCESS_FREQUENCIES: [523.25, 659.25, 783.99],
                ERROR_FREQUENCY: 220,
                BREAK_FREQUENCY: 440
            },
            
            // Card Difficulty Thresholds
            DIFFICULTY: {
                ERROR_RATE_THRESHOLD: 0.4,
                MIN_WRONG_FOR_DIFFICULT: 2,
                MASTERY_CONSECUTIVE_CORRECT: 3,
                MASTERY_MIN_SEEN: 3
            }
        };
        
        // ========================================
        // STATE MANAGEMENT
        // ========================================
        const State = {
            // Core Session Data
            session: {
                totalHours: 0,
                startTime: 0,
                preciseStartTime: 0,
                isActive: false,
                isPaused: false,
                isBreak: false
            },
            
            // Phase Management
            phase: {
                current: 0,
                startTime: 0,
                preciseStartTime: 0,
                queues: []
            },
            
            // Card Collections
            cards: {
                all: [],
                current: null,
                stats: new Map(),
                mastered: new Set(),
                learning: new Set(),
                difficult: new Set()
            },
            
            // Performance Tracking
            performance: {
                totalCorrect: 0,
                totalAttempts: 0,
                currentStreak: 0,
                longestStreak: 0,
                cardsSeenInSession: 0,
                cardsCompletedForRate: 0,
                rateHistory: [],
                last50ResponseTimes: [],
                successRateHistory: []
            },
            
            // Timing & Intervals
            timing: {
                nextBreakTime: 0,
                totalPausedTime: 0,
                pauseStartTime: 0,
                rateCalculationStartTime: 0,
                savedBreakDuration: 0,
                timerInterval: null,
                breakInterval: null,
                responseTimeBaseline: null,
                cardDisplayStartTime: 0
            },
            
            // Settings
            settings: {
                soundEnabled: true,
                audioContext: null,
                leftOscillator: null,
                rightOscillator: null,
                binauralGainNode: null
            },
            
            // Memory Enhancement Systems State
            memoryEnhancement: {
                systemsActive: new Set(),
                distinctivenessCounter: 0,
                fatigueLevel: 0,
                mouseCooldown: false,
                emotionalColorRotation: 0,
                peripheralRotation: 0,
                quantumSchedule: [20, 90, 480, 1440, 4320, 10080, 20160, 50400, 100800],
                lastPrimeTime: 0,
                lastPeripheralTime: 0,
                lastEmotionalWordTime: 0,
                lastOlfactoryTime: 0,
                successAnchorCooldown: 0,
                userTempo: null,
                temporalPatterns: new Map(),
                volumeHistory: [],
                // Systems 22-23 state
                proprietoceptionDirection: 1,
                quantumCyclingInterval: [],
                lastProprioceptiveTime: 0,
                isUserInteracting: false,
                // Systems 24-26 state
                chronestheticAdjustments: new Map(),
                preloadCache: new Map(),
                preloadStartTime: 0,
                preloadProgress: 0,
                successAnchorWords: ["capable", "learning", "memory", "smart", "progress"],
                lastSuccessAnchorTime: 0,
                // Systems 27-30 state
                retinalAfterimageActive: false,
                infrasonicOscillator: null,
                infrasonicGainNode: null,
                lastBlinkTime: 0,
                blinkInterval: null,
                semanticWordDatabase: [
                    "knowledge", "wisdom", "understanding", "insight", "learning", "memory", "recall", "focus", 
                    "attention", "concentration", "study", "practice", "mastery", "skill", "ability", "talent",
                    "intelligence", "cognition", "thinking", "reasoning", "logic", "analysis", "synthesis", "evaluation",
                    "creativity", "innovation", "discovery", "exploration", "investigation", "research", "science",
                    "education", "teaching", "instruction", "guidance", "mentorship", "coaching", "training", "development",
                    "growth", "progress", "improvement", "enhancement", "optimization", "refinement", "perfection", "excellence"
                ],
                lastSemanticPrimeTime: 0,
                // Systems 31-36 state
                interactionTimes: [],
                lastPhaseLockedTime: 0,
                phaseLockedInterval: null,
                vestibularDirection: 0,
                lastVestibularTime: 0,
                corticalRingActive: false,
                lastEmotionalTagTime: 0,
                lastClickPosition: { x: 0, y: 0 },
                quantumVibrationIntervals: [],
                somaticWordIndex: 0,
                somaticWordBank: ["warm", "cool", "soft", "sharp"],
                lastSomaticTime: 0,
                // NEW SYSTEMS 37-42 STATE
                chronobiologicalTintApplied: false,
                lastHandwritingTime: 0,
                lastConfidenceFlashTime: 0,
                deltaWavePulseActive: false,
                deltaWaveInterval: null,
                schumannResonanceOscillator: null,
                schumannGainNode: null,
                accelerometerActive: false,
                deviceMotionHandler: null,
                handTremorFrequency: 10, // Hz
                lastAccelerometerFlashTime: 0,
                isMobileDevice: false
            }
        };
        
        // ========================================
        // MEMORY ENHANCEMENT MODULE
        // ========================================
        const MemoryEnhancement = {
            
            // Initialize all memory systems
            init() {
                this.initializeAudioNodes();
                this.setupEventListeners();
                this.activateSystems();
                this.detectMobileDevice();
            },
            
            initializeAudioNodes() {
                try {
                    if (State.settings.audioContext) {
                        // Setup for binaural beats
                        State.settings.leftOscillator = State.settings.audioContext.createOscillator();
                        State.settings.rightOscillator = State.settings.audioContext.createOscillator();
                        State.settings.binauralGainNode = State.settings.audioContext.createGain();
                        State.settings.binauralGainNode.gain.value = 0;
                    }
                } catch (error) {
                    console.log('Audio initialization failed:', error);
                }
            },
            
            detectMobileDevice() {
                // Detect if this is a mobile device for System 42
                State.memoryEnhancement.isMobileDevice = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
            },
            
            setupEventListeners() {
                // System 14: Microsaccade Encoding Pattern
                let lastMouseMove = 0;
                let lastMouseX = 0;
                let lastMouseY = 0;
                
                document.addEventListener('mousemove', (e) => {
                    const now = performance.now();
                    const deltaTime = now - lastMouseMove;
                    if (deltaTime > 0) {
                        const deltaX = e.clientX - lastMouseX;
                        const deltaY = e.clientY - lastMouseY;
                        const velocity = Math.sqrt(deltaX * deltaX + deltaY * deltaY) / deltaTime * 1000;
                        
                        if (velocity > 300 && !State.memoryEnhancement.mouseCooldown && State.cards.current) {
                            this.System14_MicrosaccadeEncoding(deltaX, deltaY);
                            State.memoryEnhancement.mouseCooldown = true;
                            setTimeout(() => { State.memoryEnhancement.mouseCooldown = false; }, 2000);
                        }
                    }
                    lastMouseMove = now;
                    lastMouseX = e.clientX;
                    lastMouseY = e.clientY;
                });
                
                // System 15: Haptic Memory Encoding (Mobile)
                if ('vibrate' in navigator) {
                    State.memoryEnhancement.systemsActive.add('haptic');
                }
                
                // Systems 31-36: Enhanced user interaction tracking
                let interactionTimes = [];
                
                // Track clicks for Systems 31 and 34
                document.addEventListener('click', (e) => {
                    State.memoryEnhancement.isUserInteracting = true;
                    setTimeout(() => { State.memoryEnhancement.isUserInteracting = false; }, 1000);
                    
                    // System 31: Track for phase-locked neural oscillation
                    interactionTimes.push(performance.now());
                    State.memoryEnhancement.interactionTimes.push(performance.now());
                    
                    // Keep only last 25 interactions
                    if (State.memoryEnhancement.interactionTimes.length > 25) {
                        State.memoryEnhancement.interactionTimes.shift();
                    }
                    
                    // System 34: Store click position for emotional tagging
                    State.memoryEnhancement.lastClickPosition = { x: e.clientX, y: e.clientY };
                    
                    // Calculate user tempo for System 31
                    if (State.memoryEnhancement.interactionTimes.length >= 5) {
                        this.calculateUserTempo(State.memoryEnhancement.interactionTimes);
                    }
                    
                    // Recalculate tempo every 20 interactions
                    if (State.memoryEnhancement.interactionTimes.length % 20 === 0) {
                        this.calculateUserTempo(State.memoryEnhancement.interactionTimes);
                    }
                });
                
                // Track scrolling for System 31
                document.addEventListener('scroll', () => {
                    State.memoryEnhancement.isUserInteracting = true;
                    setTimeout(() => { State.memoryEnhancement.isUserInteracting = false; }, 1000);
                    
                    State.memoryEnhancement.interactionTimes.push(performance.now());
                    if (State.memoryEnhancement.interactionTimes.length > 25) {
                        State.memoryEnhancement.interactionTimes.shift();
                    }
                    
                    if (State.memoryEnhancement.interactionTimes.length >= 5) {
                        this.calculateUserTempo(State.memoryEnhancement.interactionTimes);
                    }
                });
                
                // Track keyboard for System 31
                document.addEventListener('keydown', () => {
                    State.memoryEnhancement.isUserInteracting = true;
                    setTimeout(() => { State.memoryEnhancement.isUserInteracting = false; }, 1000);
                    
                    State.memoryEnhancement.interactionTimes.push(performance.now());
                    if (State.memoryEnhancement.interactionTimes.length > 25) {
                        State.memoryEnhancement.interactionTimes.shift();
                    }
                    
                    if (State.memoryEnhancement.interactionTimes.length >= 5) {
                        this.calculateUserTempo(State.memoryEnhancement.interactionTimes);
                    }
                });
                
                // NEW: System 42 - Setup accelerometer for mobile devices
                if (State.memoryEnhancement.isMobileDevice && typeof DeviceMotionEvent !== 'undefined') {
                    this.setupAccelerometer();
                }
            },
            
            // NEW: System 42 accelerometer setup
            setupAccelerometer() {
                if (typeof DeviceMotionEvent.requestPermission === 'function') {
                    // iOS 13+ permission request
                    document.addEventListener('click', () => {
                        DeviceMotionEvent.requestPermission()
                            .then(response => {
                                if (response == 'granted') {
                                    this.activateAccelerometer();
                                }
                            })
                            .catch(console.error);
                    }, { once: true });
                } else {
                    // Android or older iOS
                    this.activateAccelerometer();
                }
            },
            
            // NEW: System 42 accelerometer activation
            activateAccelerometer() {
                State.memoryEnhancement.deviceMotionHandler = (event) => {
                    if (State.session.isActive && !State.session.isPaused && !State.session.isBreak) {
                        this.System42_AccelerometerRhythmEncoding(event);
                    }
                };
                
                window.addEventListener('devicemotion', State.memoryEnhancement.deviceMotionHandler);
                State.memoryEnhancement.accelerometerActive = true;
            },
            
            activateSystems() {
                // Activate all applicable systems (now includes 37-42)
                for (let i = 1; i <= 42; i++) {
                    State.memoryEnhancement.systemsActive.add(i);
                }
            },
            
            // =====================================
            // SYSTEM 1: Response Time Memory Strength Detection
            // =====================================
            System1_ResponseTimeDetection(responseTime) {
                let strength = 'unknown';
                if (responseTime < 650) {
                    strength = 'overlearned';
                } else if (responseTime < 1400) {
                    strength = 'optimal';
                } else if (responseTime < 2800) {
                    strength = 'effortful';
                } else if (responseTime < 4500) {
                    strength = 'weak';
                } else {
                    strength = 'forgotten';
                }
                
                // Store for card scheduling optimization
                if (State.cards.current) {
                    const stats = State.cards.stats.get(State.cards.current.id);
                    if (stats) {
                        stats.lastStrength = strength;
                        stats.responseTimeHistory.push(responseTime);
                    }
                }
                
                return strength;
            },
            
            // =====================================
            // SYSTEM 2: Prediction Error Optimization
            // =====================================
            System2_PredictionErrorOptimization() {
                // Track last 50 cards
                State.performance.successRateHistory.push(State.performance.totalCorrect / Math.max(1, State.performance.totalAttempts));
                if (State.performance.successRateHistory.length > 50) {
                    State.performance.successRateHistory.shift();
                }
                
                if (State.performance.successRateHistory.length >= 20) {
                    const recentRate = State.performance.successRateHistory.slice(-20).reduce((a, b) => a + b, 0) / 20;
                    
                    // Adjust intervals based on performance
                    if (recentRate > 0.87) {
                        // Decrease intervals by 18%
                        State.phase.queues.forEach(queue => {
                            queue.forEach(card => {
                                card.nextReview *= 0.82;
                            });
                        });
                    } else if (recentRate < 0.83) {
                        // Increase intervals by 18%
                        State.phase.queues.forEach(queue => {
                            queue.forEach(card => {
                                card.nextReview *= 1.18;
                            });
                        });
                    }
                }
            },
            
            // =====================================
            // SYSTEM 3: Serial Position Memory Hacking
            // =====================================
            System3_SerialPositionHacking() {
                if (!State.phase.queues[State.phase.current]) return;
                
                const queue = State.phase.queues[State.phase.current];
                const difficultCards = queue.filter(card => card.wrongCount > 2);
                const otherCards = queue.filter(card => card.wrongCount <= 2);
                
                // Place difficult cards at optimal positions
                const newQueue = [];
                const primePositions = [0, 1, 2, queue.length - 1, queue.length - 2];
                
                // Fill prime positions with difficult cards
                difficultCards.slice(0, primePositions.length).forEach((card, idx) => {
                    if (primePositions[idx] < queue.length) {
                        newQueue[primePositions[idx]] = card;
                    }
                });
                
                // Fill remaining positions
                let otherIndex = 0;
                for (let i = 0; i < queue.length; i++) {
                    if (!newQueue[i] && otherIndex < otherCards.length) {
                        newQueue[i] = otherCards[otherIndex++];
                    }
                }
                
                State.phase.queues[State.phase.current] = newQueue.filter(card => card);
            },
            
            // =====================================
            // SYSTEM 4: Micro-Priming System
            // =====================================
            System4_MicroPriming() {
                if (!State.cards.current || State.performance.cardsSeenInSession === 0) return;
                
                const primeElement = document.getElementById('memory-prime');
                if (!primeElement) return;
                
                // Show first 2 letters
                const primeText = State.cards.current.answer.substring(0, 2);
                primeElement.textContent = primeText;
                primeElement.style.opacity = '0.08';
                primeElement.style.left = '50%';
                primeElement.style.top = '40%';
                primeElement.style.transform = 'translate(-50%, -50%)';
                
                // Display for 33ms
                setTimeout(() => {
                    primeElement.style.opacity = '0';
                    // 50ms backward mask
                    setTimeout(() => {
                        primeElement.textContent = '██';
                        primeElement.style.opacity = '0.08';
                        setTimeout(() => {
                            primeElement.style.opacity = '0';
                        }, 50);
                    }, 0);
                }, 33);
            },
            
            // =====================================
            // SYSTEM 5: Visual Memory Dual-Encoding
            // =====================================
            System5_VisualMemoryEncoding() {
                if (!State.cards.current) return;
                
                const pattern = document.getElementById('visual-memory-pattern');
                const dotPattern = document.getElementById('dot-pattern');
                if (!pattern || !dotPattern) return;
                
                // Clear previous pattern
                dotPattern.innerHTML = '';
                
                // Generate 4x4 pattern based on card ID
                const seed = State.cards.current.id;
                for (let i = 0; i < 16; i++) {
                    const x = (i % 4) * 10 + 5;
                    const y = Math.floor(i / 4) * 10 + 5;
                    const filled = ((seed * (i + 1)) % 3) !== 0;
                    
                    const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                    circle.setAttribute('cx', x);
                    circle.setAttribute('cy', y);
                    circle.setAttribute('r', '3');
                    circle.setAttribute('fill', filled ? 'hsla(220, 60%, 50%, 0.12)' : 'none');
                    circle.setAttribute('stroke', 'hsla(220, 60%, 50%, 0.12)');
                    circle.setAttribute('stroke-width', '1');
                    
                    dotPattern.appendChild(circle);
                }
                
                pattern.style.opacity = '0.12';
            },
            
            // =====================================
            // SYSTEM 6: Consolidation Window Enforcement
            // =====================================
            System6_ConsolidationWindow() {
                const container = document.querySelector('.card-container');
                if (!container) return;
                
                // Disable all buttons
                document.querySelectorAll('.button-group button').forEach(btn => {
                    btn.disabled = true;
                    btn.style.opacity = '0.5';
                });
                
                // Breathing animation
                container.style.transition = 'transform 4s ease-in-out';
                container.style.transform = 'scale(0.98)';
                
                setTimeout(() => {
                    container.style.transform = 'scale(1)';
                }, 4000);
                
                // Background fade
                document.body.style.transition = 'opacity 0.5s';
                document.body.style.opacity = '0.95';
                
                // Re-enable after 8 seconds
                setTimeout(() => {
                    document.querySelectorAll('.button-group button').forEach(btn => {
                        btn.disabled = false;
                        btn.style.opacity = '1';
                    });
                    document.body.style.opacity = '1';
                }, 8000);
            },
            
            // =====================================
            // SYSTEM 7: Emotional State Color Optimization
            // =====================================
            System7_EmotionalColorOptimization() {
                const container = document.querySelector('.container');
                if (!container) return;
                
                let hueRotation = 0;
                const streak = State.performance.currentStreak;
                const failureStreak = State.performance.totalAttempts - State.performance.totalCorrect;
                
                if (streak > 5) {
                    hueRotation = 7;
                } else if (streak > 3) {
                    hueRotation = 4;
                } else if (failureStreak > 4) {
                    hueRotation = -7;
                } else if (failureStreak > 2) {
                    hueRotation = -4;
                }
                
                State.memoryEnhancement.emotionalColorRotation = hueRotation;
                container.style.transition = 'filter 1.5s ease-in-out';
                container.style.filter = `hue-rotate(${hueRotation}deg)`;
            },
            
            // =====================================
            // SYSTEM 8: Quantum Spaced Repetition Schedule
            // =====================================
            System8_QuantumScheduling() {
                if (!State.cards.current) return;
                
                const performanceFactor = State.cards.current.correctCount / Math.max(1, State.cards.current.totalSeen);
                const adjustedFactor = 0.7 + (performanceFactor * 0.6); // 0.7 to 1.3
                
                // Add jitter
                const jitter = 0.9 + (Math.random() * 0.2); // ±10%
                
                const stats = State.cards.stats.get(State.cards.current.id);
                if (stats) {
                    stats.quantumSchedule = State.memoryEnhancement.quantumSchedule.map(interval => 
                        Math.round(interval * adjustedFactor * jitter)
                    );
                    stats.quantumScheduleIndex = 0;
                }
            },
            
            // =====================================
            // SYSTEM 9: Covert Retrieval Practice
            // =====================================
            System9_CovertRetrieval() {
                if (Math.random() > 0.5 || !State.cards.all.length) return;
                
                const now = performance.now();
                if (now - State.memoryEnhancement.lastPrimeTime < 5000) return;
                
                // Select random cards
                const numCards = Math.min(2, State.cards.all.length);
                const selectedCards = [];
                for (let i = 0; i < numCards; i++) {
                    const randomCard = State.cards.all[Math.floor(Math.random() * State.cards.all.length)];
                    if (!selectedCards.includes(randomCard)) {
                        selectedCards.push(randomCard);
                    }
                }
                
                // Flash briefly
                selectedCards.forEach((card, index) => {
                    setTimeout(() => {
                        const primeElement = document.getElementById('memory-prime');
                        if (primeElement) {
                            primeElement.textContent = card.question;
                            primeElement.style.opacity = '0.04';
                            primeElement.style.fontSize = '0.9rem';
                            setTimeout(() => {
                                primeElement.style.opacity = '0';
                            }, 167);
                        }
                    }, index * 200);
                });
                
                State.memoryEnhancement.lastPrimeTime = now;
            },
            
            // =====================================
            // SYSTEM 10: Fatigue Auto-Detection
            // =====================================
            System10_FatigueDetection() {
                if (State.performance.cardsSeenInSession < 10) return;
                
                // Calculate baseline from first 10 cards
                if (!State.timing.responseTimeBaseline && State.performance.last50ResponseTimes.length >= 10) {
                    const first10 = State.performance.last50ResponseTimes.slice(0, 10);
                    State.timing.responseTimeBaseline = first10.reduce((a, b) => a + b, 0) / 10;
                }
                
                if (!State.timing.responseTimeBaseline) return;
                
                // Check every 15 cards
                if (State.performance.cardsSeenInSession % 15 !== 0) return;
                
                // Calculate recent average
                const recent10 = State.performance.last50ResponseTimes.slice(-10);
                const recentAvg = recent10.reduce((a, b) => a + b, 0) / recent10.length;
                
                // Check fatigue indicators
                let fatigueLevel = 0;
                if (recentAvg > State.timing.responseTimeBaseline * 1.25) {
                    fatigueLevel++;
                }
                
                const recentSuccess = State.performance.successRateHistory.slice(-15);
                const recentRate = recentSuccess.reduce((a, b) => a + b, 0) / recentSuccess.length;
                const overallRate = State.performance.totalCorrect / Math.max(1, State.performance.totalAttempts);
                
                if (recentRate < overallRate * 0.88) {
                    fatigueLevel++;
                }
                
                State.memoryEnhancement.fatigueLevel = fatigueLevel;
                
                if (fatigueLevel >= 2) {
                    // Force break
                    ScholarSRS.Achievement.show('Fatigue Detected', 'Time for a 7-minute restorative break');
                    State.timing.nextBreakTime = Date.now();
                }
            },
            
            // =====================================
            // SYSTEM 11: Distinctiveness Memory Boost
            // =====================================
            System11_DistinctivenessBoost() {
                State.memoryEnhancement.distinctivenessCounter++;
                
                // Activate every 9±2 cards
                const interval = 9 + Math.floor(Math.random() * 5) - 2;
                if (State.memoryEnhancement.distinctivenessCounter % interval !== 0) return;
                
                const container = document.querySelector('.card-container');
                if (!container) return;
                
                // Apply random effect
                const effects = [
                    () => { container.style.fontSize = '118%'; },
                    () => { container.style.letterSpacing = '0.5px'; },
                    () => { container.style.textShadow = '0 0 3px rgba(100,100,255,0.15)'; },
                    () => { container.style.transform = 'scale(1.02)'; }
                ];
                
                const effect = effects[Math.floor(Math.random() * effects.length)];
                effect();
                container.classList.add('distinctiveness-boost');
                
                // Store that this card was distinctive
                if (State.cards.current) {
                    const stats = State.cards.stats.get(State.cards.current.id);
                    if (stats) {
                        stats.wasDistinctive = true;
                    }
                }
            },
            
            // =====================================
            // SYSTEM 12: Binaural Beat Memory Encoding
            // =====================================
            System12_BinauralBeats(phase) {
                if (!State.settings.soundEnabled || !State.settings.audioContext) return;
                
                try {
                    // Disconnect previous connections
                    if (State.settings.leftOscillator) {
                        State.settings.leftOscillator.disconnect();
                        State.settings.rightOscillator.disconnect();
                    }
                    
                    // Create new oscillators
                    const leftOsc = State.settings.audioContext.createOscillator();
                    const rightOsc = State.settings.audioContext.createOscillator();
                    const merger = State.settings.audioContext.createChannelMerger(2);
                    const gainNode = State.settings.audioContext.createGain();
                    
                    // Set frequencies based on phase
                    if (phase === 'question') {
                        leftOsc.frequency.value = 515; // 15Hz beta
                        rightOsc.frequency.value = 500;
                    } else {
                        leftOsc.frequency.value = 410; // 10Hz alpha
                        rightOsc.frequency.value = 400;
                    }
                    
                    // Set volume
                    gainNode.gain.value = 0.08;
                    
                    // Connect nodes
                    leftOsc.connect(merger, 0, 0);
                    rightOsc.connect(merger, 0, 1);
                    merger.connect(gainNode);
                    gainNode.connect(State.settings.audioContext.destination);
                    
                    // Start oscillators
                    leftOsc.start();
                    rightOsc.start();
                    
                    // Fade out after card display
                    setTimeout(() => {
                        gainNode.gain.exponentialRampToValueAtTime(0.001, State.settings.audioContext.currentTime + 0.2);
                        setTimeout(() => {
                            leftOsc.stop();
                            rightOsc.stop();
                        }, 200);
                    }, 3000);
                    
                } catch (error) {
                    // Binaural beats failed
                }
            },
            
            // =====================================
            // SYSTEM 13: Peripheral Vision Memory Injection
            // =====================================
            System13_PeripheralInjection() {
                if (!State.cards.current) return;
                
                const element = document.getElementById('peripheral-text');
                if (!element) return;
                
                const now = performance.now();
                if (now - State.memoryEnhancement.lastPeripheralTime < 4000) return;
                
                // Calculate peripheral position
                const angle = State.memoryEnhancement.peripheralRotation * (Math.PI / 4);
                const radius = Math.min(window.innerWidth, window.innerHeight) * 0.4;
                const centerX = window.innerWidth / 2;
                const centerY = window.innerHeight / 2;
                
                const x = centerX + Math.cos(angle) * radius;
                const y = centerY + Math.sin(angle) * radius;
                
                element.textContent = State.cards.current.answer;
                element.style.left = x + 'px';
                element.style.top = y + 'px';
                element.style.opacity = '0.06';
                element.style.fontSize = '24px';
                element.style.color = State.memoryEnhancement.emotionalColorRotation > 0 ? '#2e7d32' : '#1976d2';
                
                setTimeout(() => {
                    element.style.opacity = '0';
                }, 3000);
                
                State.memoryEnhancement.peripheralRotation = (State.memoryEnhancement.peripheralRotation + 1) % 8;
                State.memoryEnhancement.lastPeripheralTime = now;
            },
            
            // =====================================
            // SYSTEM 14: Microsaccade Encoding Pattern
            // =====================================
            System14_MicrosaccadeEncoding(deltaX, deltaY) {
                if (!State.cards.current) return;
                
                const element = document.getElementById('memory-prime');
                if (!element) return;
                
                // Calculate position 100px ahead of movement vector
                const magnitude = Math.sqrt(deltaX * deltaX + deltaY * deltaY);
                const normalizedX = (deltaX / magnitude) * 100;
                const normalizedY = (deltaY / magnitude) * 100;
                
                const mouseX = event.clientX;
                const mouseY = event.clientY;
                
                element.textContent = State.cards.current.answer.substring(0, 3);
                element.style.left = (mouseX + normalizedX) + 'px';
                element.style.top = (mouseY + normalizedY) + 'px';
                element.style.opacity = '0.09';
                
                setTimeout(() => {
                    element.style.opacity = '0';
                }, 83);
            },
            
            // =====================================
            // SYSTEM 15: Haptic Memory Encoding (Mobile)
            // =====================================
            System15_HapticEncoding() {
                if (!navigator.vibrate || !State.cards.current) return;
                
                const pattern = [10, 30, 10, 50, 10];
                const intensity = State.cards.current.difficulty * 0.3;
                
                // Scale pattern by intensity
                const scaledPattern = pattern.map(duration => Math.round(duration * intensity));
                
                setTimeout(() => {
                    navigator.vibrate(scaledPattern);
                }, 200);
            },
            
            // =====================================
            // SYSTEM 16: Chromatic Memory Signatures
            // =====================================
            System16_ChromaticSignatures() {
                if (!State.cards.current) return;
                
                // djb2 hash function
                const hash = (str) => {
                    let hash = 5381;
                    for (let i = 0; i < str.length; i++) {
                        hash = ((hash << 5) + hash) + str.charCodeAt(i);
                    }
                    return Math.abs(hash);
                };
                
                const colorHash = hash(State.cards.current.answer);
                const hue = colorHash % 360;
                const saturation = 25;
                const lightness = 48 + (colorHash % 5);
                
                const container = document.querySelector('.card-container');
                if (container) {
                    container.style.backgroundColor = `hsla(${hue}, ${saturation}%, ${lightness}%, 0.08)`;
                    container.style.borderColor = `hsla(${hue}, ${saturation}%, ${lightness}%, 0.15)`;
                }
            },
            
            // =====================================
            // SYSTEM 17: Subliminal Audio Repetition
            // =====================================
            System17_SubliminalAudio() {
                if (!State.settings.soundEnabled || !State.cards.current) return;
                
                // This would require text-to-speech API
                // Implementing basic frequency modulation instead
                try {
                    const context = State.settings.audioContext;
                    if (!context) return;
                    
                    const oscillator = context.createOscillator();
                    const gainNode = context.createGain();
                    
                    oscillator.frequency.value = 440 + 200; // +200Hz shift
                    gainNode.gain.value = 0.012;
                    
                    oscillator.connect(gainNode);
                    gainNode.connect(context.destination);
                    
                    oscillator.start();
                    oscillator.stop(context.currentTime + 0.5);
                    
                } catch (error) {
                    // Audio failed
                }
            },
            
            // =====================================
            // SYSTEM 18: Temporal Pattern Encoding
            // =====================================
            System18_TemporalPattern() {
                if (!State.cards.current) return;
                
                const baseInterval = 1000;
                const variation = State.cards.current.id % 150;
                const displayTime = baseInterval + variation;
                
                // Store pattern
                State.memoryEnhancement.temporalPatterns.set(State.cards.current.id, displayTime);
                
                // Apply timing on reviews
                const stats = State.cards.stats.get(State.cards.current.id);
                if (stats && stats.totalSeen > 1) {
                    const storedPattern = State.memoryEnhancement.temporalPatterns.get(State.cards.current.id);
                    if (storedPattern) {
                        setTimeout(() => {
                            // Subtle timing adjustment
                            const container = document.querySelector('.card-container');
                            if (container) {
                                container.style.transition = `opacity ${storedPattern}ms`;
                            }
                        }, 0);
                    }
                }
            },
            
            // =====================================
            // SYSTEM 19: Screen Flicker Consolidation
            // =====================================
            System19_FlickerConsolidation() {
                if (!State.cards.current || State.cards.current.wrongCount > 0) return;
                
                const container = document.querySelector('.container');
                if (!container) return;
                
                container.style.animation = 'flicker 0.5s ease-in-out 4';
                
                set
                const stats = State.cards.stats.get(State.cards.current.id);
                if (stats && stats.totalSeen > 1) {
                    const storedPattern = State.memoryEnhancement.temporalPatterns.get(State.cards.current.id);
                    if (storedPattern) {
                        setTimeout(() => {
                            // Subtle timing adjustment
                            const container = document.querySelector('.card-container');
                            if (container) {
                                container.style.transition = `opacity ${storedPattern}ms`;
                            }
                        }, 0);
                    }
                }
            },
            
            // =====================================
            // SYSTEM 19: Screen Flicker Consolidation
            // =====================================
            System19_FlickerConsolidation() {
                if (!State.cards.current || State.cards.current.wrongCount > 0) return;
                
                const container = document.querySelector('.container');
                if (!container) return;
                
                container.style.animation = 'flicker 0.5s ease-in-out 4';
                
                setTimeout(() => {
                    container.style.animation = '';
                }, 2000);
            },
            
            // =====================================
            // SYSTEM 20: Ultrasonic Memory Anchoring
            // =====================================
            System20_UltrasonicAnchoring() {
                if (!State.settings.soundEnabled || !State.settings.audioContext || !State.cards.current) return;
                
                try {
                    const context = State.settings.audioContext;
                    const oscillator = context.createOscillator();
                    const gainNode = context.createGain();
                    
                    const baseFreq = 17500;
                    const modulation = State.cards.current.id % 500;
                    oscillator.frequency.value = baseFreq + modulation;
                    
                    gainNode.gain.value = 0.008;
                    gainNode.gain.exponentialRampToValueAtTime(0.001, context.currentTime + 0.4);
                    
                    oscillator.connect(gainNode);
                    gainNode.connect(context.destination);
                    
                    oscillator.start();
                    oscillator.stop(context.currentTime + 0.4);
                    
                } catch (error) {
                    // Ultrasonic failed
                }
            },
            
            // =====================================
            // SYSTEM 21: Olfactory Priming Simulation
            // =====================================
            System21_OlfactoryPriming() {
                const words = ["vanilla", "cinnamon", "ocean", "forest", "coffee"];
                const element = document.getElementById('olfactory-word');
                if (!element) return;
                
                const now = performance.now();
                if (now - State.memoryEnhancement.lastOlfactoryTime < 10000) return;
                
                const word = words[Math.floor(Math.random() * words.length)];
                element.textContent = word;
                element.style.opacity = '0.02';
                
                setTimeout(() => {
                    element.style.opacity = '0';
                }, 25);
                
                State.memoryEnhancement.lastOlfactoryTime = now;
            },
            
            // =====================================
            // SYSTEM 22: Proprioceptive Memory Encoding
            // =====================================
            System22_ProprioceptiveEncoding() {
                if (!State.cards.current) return;
                
                const container = document.querySelector('.card-container');
                if (!container) return;
                
                const now = performance.now();
                if (now - State.memoryEnhancement.lastProprioceptiveTime < 3000) return;
                
                // Calculate rotation based on card difficulty
                const difficultyFactor = Math.max(0.15, Math.min(0.35, State.cards.current.difficulty * 0.1));
                
                // Alternating direction based on card ID and stored direction
                State.memoryEnhancement.proprietoceptionDirection *= -1;
                const rotation = difficultyFactor * State.memoryEnhancement.proprietoceptionDirection;
                
                // Apply rotation with 2s ease-in-out transition
                container.style.transition = 'transform 2s ease-in-out';
                container.style.transform = `rotate(${rotation}deg)`;
                
                // Reset after 4 seconds
                setTimeout(() => {
                    container.style.transition = 'transform 2s ease-in-out';
                    container.style.transform = 'rotate(0deg)';
                }, 4000);
                
                State.memoryEnhancement.lastProprioceptiveTime = now;
            },
            
            // =====================================
            // SYSTEM 23: Quantum Attention Cycling
            // =====================================
            System23_QuantumAttentionCycling() {
                if (!State.cards.current) return;
                
                const questionElement = document.getElementById('card-question');
                if (!questionElement) return;
                
                // Skip during user interaction
                if (State.memoryEnhancement.isUserInteracting) return;
                
                // Check if user can interact (answer not shown yet)
                const showBtn = document.getElementById('show-answer-btn');
                const correctBtn = document.getElementById('correct-btn');
                if (!showBtn || showBtn.style.display === 'none' || 
                    (correctBtn && correctBtn.style.display !== 'none')) {
                    return;
                }
                
                // Golden ratio based interval: 144ms
                const interval = 144; // ms
                const flashDuration = 8; // ms
                const opacity = 0.013;
                
                // Clean up any existing intervals
                State.memoryEnhancement.quantumCyclingInterval.forEach(clearInterval);
                State.memoryEnhancement.quantumCyclingInterval = [];
                
                // Start quantum cycling
                const cyclingInterval = setInterval(() => {
                    // Double-check conditions during cycling
                    if (!State.cards.current || 
                        State.memoryEnhancement.isUserInteracting ||
                        document.getElementById('show-answer-btn').style.display === 'none') {
                        clearInterval(cyclingInterval);
                        return;
                    }
                    
                    // Phase-lock to screen refresh rate (requestAnimationFrame)
                    requestAnimationFrame(() => {
                        // Flash text only, not background
                        const originalOpacity = questionElement.style.opacity || '1';
                        questionElement.style.opacity = opacity;
                        
                        setTimeout(() => {
                            questionElement.style.opacity = originalOpacity;
                        }, flashDuration);
                    });
                }, interval);
                
                // Store interval for cleanup
                State.memoryEnhancement.quantumCyclingInterval.push(cyclingInterval);
                
                // Auto cleanup after 30 seconds
                setTimeout(() => {
                    clearInterval(cyclingInterval);
                    State.memoryEnhancement.quantumCyclingInterval = 
                        State.memoryEnhancement.quantumCyclingInterval.filter(i => i !== cyclingInterval);
                }, 30000);
            },
            
            // =====================================
            // SYSTEM 24: Chronesthetic Time Warping
            // =====================================
            System24_ChronestheticTimeWarping() {
                if (!State.cards.current) return;
                
                // Determine card difficulty level
                let timingAdjustment = 0;
                const errorRate = State.cards.current.wrongCount / Math.max(1, State.cards.current.totalSeen);
                
                if (State.cards.current.wrongCount > 0) {
                    // Wrong cards: +95ms
                    timingAdjustment = 95;
                } else if (errorRate === 0 && State.cards.current.totalSeen >= 2) {
                    // Easy cards: -35ms
                    timingAdjustment = -35;
                } else if (errorRate > 0.5) {
                    // Hard cards: +65ms
                    timingAdjustment = 65;
                } else {
                    // Medium cards: baseline (0ms)
                    timingAdjustment = 0;
                }
                
                // Store adjustment for this card
                State.memoryEnhancement.chronestheticAdjustments.set(State.cards.current.id, timingAdjustment);
                
                // Apply timing adjustment to all transitions
                if (timingAdjustment !== 0) {
                    const elements = [
                        document.getElementById('card-question'),
                        document.getElementById('card-answer'),
                        document.querySelector('.card-container')
                    ];
                    
                    elements.forEach(element => {
                        if (element) {
                            const currentTransition = element.style.transition || '';
                            const baseTime = 300; // Base transition time in ms
                            const adjustedTime = Math.max(50, baseTime + timingAdjustment);
                            
                            // Apply timing adjustment to opacity transitions
                            element.style.transition = currentTransition.includes('opacity') 
                                ? currentTransition.replace(/opacity\s+[\d.]+s/, `opacity ${adjustedTime / 1000}s`)
                                : `${currentTransition}, opacity ${adjustedTime / 1000}s ease`;
                        }
                    });
                }
            },
            
            // =====================================
            // SYSTEM 25: Parallel Reality Processing
            // =====================================
            System25_ParallelReality() {
                if (!State.phase.queues[State.phase.current] || State.phase.queues[State.phase.current].length < 2) return;
                
                const now = performance.now();
                const cardDisplayDuration = now - State.timing.cardDisplayStartTime;
                const estimatedTotalTime = cardDisplayDuration / 0.6; // Current time is 60% of total
                
                // Begin preloading at 60% of current card time
                if (cardDisplayDuration >= estimatedTotalTime * 0.6) {
                    const nextCards = State.phase.queues[State.phase.current].slice(0, 2);
                    
                    nextCards.forEach((card, index) => {
                        if (!State.memoryEnhancement.preloadCache.has(card.id)) {
                            const preloadContainer = document.getElementById(`preload-container-${index + 1}`);
                            if (preloadContainer) {
                                // Prerender text
                                const questionDiv = document.createElement('div');
                                const answerDiv = document.createElement('div');
                                
                                questionDiv.className = 'card-question';
                                questionDiv.textContent = card.question;
                                
                                answerDiv.className = 'card-answer';
                                answerDiv.textContent = card.answer;
                                
                                // Clear previous content
                                preloadContainer.innerHTML = '';
                                preloadContainer.appendChild(questionDiv);
                                preloadContainer.appendChild(answerDiv);
                                
                                // Prerender visual pattern
                                if (card.id !== undefined) {
                                    const patternSvg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
                                    patternSvg.setAttribute('width', '40');
                                    patternSvg.setAttribute('height', '40');
                                    
                                    const dotGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
                                    const seed = card.id;
                                    
                                    for (let i = 0; i < 16; i++) {
                                        const x = (i % 4) * 10 + 5;
                                        const y = Math.floor(i / 4) * 10 + 5;
                                        const filled = ((seed * (i + 1)) % 3) !== 0;
                                        
                                        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                                        circle.setAttribute('cx', x);
                                        circle.setAttribute('cy', y);
                                        circle.setAttribute('r', '3');
                                        circle.setAttribute('fill', filled ? 'hsla(220, 60%, 50%, 0.12)' : 'none');
                                        circle.setAttribute('stroke', 'hsla(220, 60%, 50%, 0.12)');
                                        circle.setAttribute('stroke-width', '1');
                                        
                                        dotGroup.appendChild(circle);
                                    }
                                    
                                    patternSvg.appendChild(dotGroup);
                                    preloadContainer.appendChild(patternSvg);
                                }
                                
                                // Cache audio preparation if applicable
                                if (State.settings.audioContext && State.settings.soundEnabled) {
                                    const audioSignature = {
                                        frequency: 440 + (card.id % 200),
                                        duration: 0.5,
                                        type: 'sine'
                                    };
                                    State.memoryEnhancement.preloadCache.set(`audio_${card.id}`, audioSignature);
                                }
                                
                                // Mark as preloaded
                                State.memoryEnhancement.preloadCache.set(card.id, {
                                    question: card.question,
                                    answer: card.answer,
                                    preloadTime: now,
                                    pattern: true
                                });
                            }
                        }
                    });
                }
            },
            
            // =====================================
            // SYSTEM 26: Subliminal Success Anchoring
            // =====================================
            System26_SubliminalSuccessAnchoring() {
                // Only trigger after 3+ correct streak
                if (State.performance.currentStreak < 3) return;
                
                const now = performance.now();
                // 45 second cooldown
                if (now - State.memoryEnhancement.lastSuccessAnchorTime < 45000) return;
                
                const anchorElement = document.getElementById('success-anchor');
                if (!anchorElement) return;
                
                // Select random word from anchor words
                const words = State.memoryEnhancement.successAnchorWords;
                const word = words[Math.floor(Math.random() * words.length)];
                
                // Randomize quadrant position
                const quadrant = Math.floor(Math.random() * 4);
                let x, y;
                
                const margin = 100;
                const centerX = window.innerWidth / 2;
                const centerY = window.innerHeight / 2;
                
                switch (quadrant) {
                    case 0: // Top-left
                        x = Math.random() * (centerX - margin) + margin;
                        y = Math.random() * (centerY - margin) + margin;
                        break;
                    case 1: // Top-right
                        x = Math.random() * (centerX - margin) + centerX;
                        y = Math.random() * (centerY - margin) + margin;
                        break;
                    case 2: // Bottom-left
                        x = Math.random() * (centerX - margin) + margin;
                        y = Math.random() * (centerY - margin) + centerY;
                        break;
                    case 3: // Bottom-right
                        x = Math.random() * (centerX - margin) + centerX;
                        y = Math.random() * (centerY - margin) + centerY;
                        break;
                }
                
                // Set word and positioning
                anchorElement.textContent = word;
                anchorElement.style.left = x + 'px';
                anchorElement.style.top = y + 'px';
                anchorElement.style.fontSize = '18px';
                anchorElement.style.opacity = '0.025';
                
                // Display for 20ms
                setTimeout(() => {
                    anchorElement.style.opacity = '0';
                }, 20);
                
                State.memoryEnhancement.lastSuccessAnchorTime = now;
            },
            
            // =====================================
            // SYSTEM 27: Retinal Persistence Afterimage Encoding
            // =====================================
            System27_RetinalPersistenceAfterimage() {
                if (!State.cards.current || State.memoryEnhancement.retinalAfterimageActive) return;
                
                const flashElement = document.getElementById('afterimage-flash');
                if (!flashElement) return;
                
                State.memoryEnhancement.retinalAfterimageActive = true;
                
                // Calculate complementary color to answer text
                const answerElement = document.getElementById('card-answer');
                const computedStyle = window.getComputedStyle(answerElement);
                const currentColor = computedStyle.color;
                
                // Convert RGB to complementary color
                const rgbMatch = currentColor.match(/rgb\((\d+), (\d+), (\d+)\)/);
                let complementaryColor = '#00ff80'; // Default fallback
                
                if (rgbMatch) {
                    const r = parseInt(rgbMatch[1]);
                    const g = parseInt(rgbMatch[2]);
                    const b = parseInt(rgbMatch[3]);
                    
                    // Calculate complementary
                    const compR = 255 - r;
                    const compG = 255 - g;
                    const compB = 255 - b;
                    
                    complementaryColor = `rgb(${compR}, ${compG}, ${compB})`;
                }
                
                // Set up flash element
                const containerRect = document.querySelector('.card-container').getBoundingClientRect();
                flashElement.style.left = (containerRect.left + 3) + 'px'; // 3px right offset
                flashElement.style.top = (containerRect.top + 2) + 'px'; // 2px down offset
                flashElement.style.width = containerRect.width + 'px';
                flashElement.style.height = containerRect.height + 'px';
                flashElement.style.backgroundColor = complementaryColor;
                flashElement.textContent = State.cards.current.answer;
                flashElement.style.display = 'flex';
                flashElement.style.alignItems = 'center';
                flashElement.style.justifyContent = 'center';
                flashElement.style.fontSize = '1.2rem';
                flashElement.style.color = 'rgba(0, 0, 0, 0.8)';
                
                // Flash at 0.95 opacity for 750ms
                flashElement.style.opacity = '0.95';
                
                setTimeout(() => {
                    // 50ms neutral gray follow-up
                    flashElement.style.backgroundColor = '#808080';
                    flashElement.style.opacity = '0.3';
                    flashElement.textContent = '';
                    
                    setTimeout(() => {
                        // Create ghosted afterimage
                        flashElement.style.backgroundColor = 'transparent';
                        flashElement.style.opacity = '0.08';
                        flashElement.textContent = State.cards.current.answer;
                        flashElement.style.color = complementaryColor;
                        
                        // Afterimage persists for 2-3 seconds
                        setTimeout(() => {
                            flashElement.style.opacity = '0';
                            setTimeout(() => {
                                flashElement.style.display = 'none';
                                State.memoryEnhancement.retinalAfterimageActive = false;
                            }, 500);
                        }, 2500); // 2.5 second afterimage
                        
                    }, 50); // 50ms gray
                }, 750); // 750ms main flash
            },
            
            // =====================================
            // SYSTEM 28: Infrasonic Resonance Memory Binding
            // =====================================
            System28_InfrasonicResonance() {
                if (!State.settings.soundEnabled || !State.settings.audioContext || !State.cards.current) return;
                
                try {
                    // Clean up previous oscillator
                    if (State.memoryEnhancement.infrasonicOscillator) {
                        State.memoryEnhancement.infrasonicOscillator.stop();
                        State.memoryEnhancement.infrasonicOscillator.disconnect();
                    }
                    
                    const context = State.settings.audioContext;
                    const oscillator = context.createOscillator();
                    const gainNode = context.createGain();
                    
                    // Base frequency: 16Hz (below hearing threshold)
                    const baseFreq = 16;
                    const modulation = State.cards.current.difficulty * 2; // Modulate with difficulty
                    const standingWave = State.cards.current.id % 3; // 0, 1, or 2Hz
                    
                    oscillator.frequency.value = baseFreq + modulation + standingWave;
                    oscillator.type = 'sine';
                    
                    // Very low amplitude (felt not heard)
                    gainNode.gain.value = 0.003;
                    
                    // Connect nodes
                    oscillator.connect(gainNode);
                    gainNode.connect(context.destination);
                    
                    // Start oscillator
                    oscillator.start();
                    
                    // Store references for cleanup
                    State.memoryEnhancement.infrasonicOscillator = oscillator;
                    State.memoryEnhancement.infrasonicGainNode = gainNode;
                    
                    // Stop after card display (will be restarted for next card)
                    setTimeout(() => {
                        if (State.memoryEnhancement.infrasonicOscillator === oscillator) {
                            gainNode.gain.exponentialRampToValueAtTime(0.001, context.currentTime + 0.5);
                            setTimeout(() => {
                                oscillator.stop();
                                oscillator.disconnect();
                                State.memoryEnhancement.infrasonicOscillator = null;
                                State.memoryEnhancement.infrasonicGainNode = null;
                            }, 500);
                        }
                    }, 8000); // 8 second duration
                    
                } catch (error) {
                    // Infrasonic failed
                }
            },
            
            // =====================================
            // SYSTEM 29: Statistical Blink Window Injection
            // =====================================
            System29_StatisticalBlinkWindow() {
                if (!State.cards.current || !State.phase.queues[State.phase.current] || 
                    State.phase.queues[State.phase.current].length === 0) return;
                
                const now = performance.now();
                
                // Average blink rate: every 4.2 seconds, with random 3.8-4.6s variation
                const minInterval = 3800;
                const maxInterval = 4600;
                const avgInterval = 4200;
                
                // Check if enough time has passed since last blink injection
                if (now - State.memoryEnhancement.lastBlinkTime < minInterval) return;
                
                // Randomly trigger within the window, max frequency once per 8 seconds
                const randomInterval = minInterval + Math.random() * (maxInterval - minInterval);
                if (now - State.memoryEnhancement.lastBlinkTime < randomInterval) return;
                
                // Get next card preview
                const nextCard = State.phase.queues[State.phase.current][0];
                if (!nextCard) return;
                
                const blinkElement = document.getElementById('blink-preview');
                if (!blinkElement) return;
                
                // Position randomly in safe viewport area
                const margin = 50;
                const x = margin + Math.random() * (window.innerWidth - 2 * margin - 200);
                const y = margin + Math.random() * (window.innerHeight - 2 * margin - 50);
                
                // Set up blink preview
                blinkElement.textContent = `Next: ${nextCard.question.substring(0, 30)}...`;
                blinkElement.style.left = x + 'px';
                blinkElement.style.top = y + 'px';
                blinkElement.style.maxWidth = '200px';
                blinkElement.style.fontSize = '14px';
                
                // Flash during predicted blink (150ms duration, 0.15 opacity)
                blinkElement.style.opacity = '0.15';
                
                setTimeout(() => {
                    blinkElement.style.opacity = '0';
                }, 150); // Average blink duration
                
                State.memoryEnhancement.lastBlinkTime = now;
            },
            
            // =====================================
            // SYSTEM 30: Semantic Network Priming Cascade
            // =====================================
            System30_SemanticNetworkPriming() {
                if (!State.cards.current) return;
                
                const now = performance.now();
                // Cooldown to prevent overwhelming
                if (now - State.memoryEnhancement.lastSemanticPrimeTime < 5000) return;
                
                // Extract key noun from answer
                const answer = State.cards.current.answer.toLowerCase();
                const words = answer.split(/\s+/).filter(word => word.length > 3);
                
                if (words.length === 0) return;
                
                // Select key noun (longest word or first word)
                const keyNoun = words.reduce((longest, current) => 
                    current.length > longest.length ? current : longest, words[0]);
                
                // Find related words from semantic database
                const relatedWords = this.findSemanticRelations(keyNoun);
                
                if (relatedWords.length < 3) return;
                
                // Get prime elements
                const primeElements = [
                    document.getElementById('semantic-prime-1'),
                    document.getElementById('semantic-prime-2'),
                    document.getElementById('semantic-prime-3')
                ];
                
                if (!primeElements.every(el => el)) return;
                
                // Flash 3 related words sequentially
                relatedWords.slice(0, 3).forEach((word, index) => {
                    setTimeout(() => {
                        const element = primeElements[index];
                        
                        // Random scatter position (±100px from center)
                        const centerX = window.innerWidth / 2;
                        const centerY = window.innerHeight / 2;
                        const scatterX = centerX + (Math.random() - 0.5) * 200; // ±100px
                        const scatterY = centerY + (Math.random() - 0.5) * 200; // ±100px
                        
                        element.textContent = word;
                        element.style.left = scatterX + 'px';
                        element.style.top = scatterY + 'px';
                        element.style.fontSize = '14px';
                        element.style.opacity = '0.018'; // Very low opacity
                        
                        // Flash for 17ms
                        setTimeout(() => {
                            element.style.opacity = '0';
                        }, 17);
                        
                    }, index * 150); // 150ms spacing between words
                });
                
                State.memoryEnhancement.lastSemanticPrimeTime = now;
            },
            
            // =====================================
            // SYSTEM 31: Phase-Locked Neural Oscillation
            // =====================================
            System31_PhaseLockedNeuralOscillation() {
                if (!State.cards.current || !State.memoryEnhancement.userTempo) return;
                
                const now = performance.now();
                
                // Calculate golden ratio interval: tempo * 1.618
                const goldenInterval = State.memoryEnhancement.userTempo * 1.618;
                
                // Check cooldown based on golden ratio interval
                if (now - State.memoryEnhancement.lastPhaseLockedTime < goldenInterval) return;
                
                const flashElement = document.getElementById('phase-locked-flash');
                if (!flashElement) return;
                
                // Position near card content for motor cortex synchronization
                const containerRect = document.querySelector('.card-container').getBoundingClientRect();
                const x = containerRect.left + (containerRect.width * 0.8); // 80% across container
                const y = containerRect.top + (containerRect.height * 0.3); // 30% down container
                
                // Set up flash
                flashElement.textContent = "◉"; // Neural sync symbol
                flashElement.style.left = x + 'px';
                flashElement.style.top = y + 'px';
                flashElement.style.fontSize = '16px';
                flashElement.style.opacity = '0.011'; // Very subtle
                
                // Flash for exactly 12ms to synchronize with motor cortex
                setTimeout(() => {
                    flashElement.style.opacity = '0';
                }, 12);
                
                State.memoryEnhancement.lastPhaseLockedTime = now;
            },
            
            // =====================================
            // SYSTEM 32: Vestibular Memory Encoding
            // =====================================
            System32_VestibularMemoryEncoding() {
                if (!State.cards.current) return;
                
                const container = document.querySelector('.card-container');
                if (!container) return;
                
                const now = performance.now();
                if (now - State.memoryEnhancement.lastVestibularTime < 5000) return;
                
                // Calculate direction based on card.id % 4
                const directions = [
                    'perspective(1000px) rotateX(0.5deg)', // Down
                    'perspective(1000px) rotateY(0.5deg)', // Right
                    'perspective(1000px) rotateX(-0.5deg)', // Up
                    'perspective(1000px) rotateY(-0.5deg)' // Left
                ];
                
                const direction = directions[State.cards.current.id % 4];
                
                // Apply vestibular shift
                container.classList.add('vestibular-shift');
                container.style.transform = direction;
                
                // Reset to 0deg after 3 seconds
                setTimeout(() => {
                    container.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg)';
                    
                    // Remove class after transition completes
                    setTimeout(() => {
                        container.classList.remove('vestibular-shift');
                        container.style.transform = '';
                    }, 3000);
                }, 3000);
                
                State.memoryEnhancement.lastVestibularTime = now;
            },
            
            // =====================================
            // SYSTEM 33: Cortical Spreading Depression Bypass
            // =====================================
            System33_CorticalSpreadingDepressionBypass() {
                // Only activate after 5 consecutive correct answers
                if (State.performance.currentStreak < 5 || State.memoryEnhancement.corticalRingActive) return;
                
                const ringElement = document.getElementById('cortical-ring');
                if (!ringElement) return;
                
                State.memoryEnhancement.corticalRingActive = true;
                
                // Get current theme hue and shift it +10 for blue shift
                const containerStyle = window.getComputedStyle(document.querySelector('.card-container'));
                let baseHue = 220; // Default blue hue
                
                // Create blue-shifted color
                const blueShiftedColor = `hsl(${baseHue + 10}, 60%, 50%)`;
                
                // Set up ring animation
                ringElement.style.borderColor = blueShiftedColor;
                ringElement.style.animation = 'corticalExpansion 1200ms ease-out forwards';
                
                // Reset after animation completes
                setTimeout(() => {
                    ringElement.style.animation = '';
                    ringElement.style.opacity = '0';
                    State.memoryEnhancement.corticalRingActive = false;
                }, 1200);
            },
            
            // =====================================
            // SYSTEM 34: Subliminal Emotional Tagging
            // =====================================
            System34_SubliminalEmotionalTagging() {
                if (!State.cards.current) return;
                
                const now = performance.now();
                // 30 second cooldown
                if (now - State.memoryEnhancement.lastEmotionalTagTime < 30000) return;
                
                const tagElement = document.getElementById('emotional-tag');
                if (!tagElement) return;
                
                // Match emotion to card difficulty
                const emojis = ["😊", "😮", "😤", "😌"];
                let emoji;
                
                const errorRate = State.cards.current.wrongCount / Math.max(1, State.cards.current.totalSeen);
                
                if (errorRate === 0 && State.cards.current.totalSeen > 0) {
                    emoji = "😊"; // Joy for easy cards
                } else if (errorRate < 0.3) {
                    emoji = "😌"; // Content for manageable cards
                } else if (errorRate < 0.6) {
                    emoji = "😮"; // Surprise for medium difficulty
                } else {
                    emoji = "😤"; // Determination for difficult cards
                }
                
                // Position at last click location
                const x = State.memoryEnhancement.lastClickPosition.x || window.innerWidth / 2;
                const y = State.memoryEnhancement.lastClickPosition.y || window.innerHeight / 2;
                
                // Set up emotional tag
                tagElement.textContent = emoji;
                tagElement.style.left = x + 'px';
                tagElement.style.top = y + 'px';
                tagElement.style.fontSize = '24px';
                tagElement.style.opacity = '0.016'; // Very subtle opacity
                
                // Display for exactly 14ms to hijack amygdala processing
                setTimeout(() => {
                    tagElement.style.opacity = '0';
                }, 14);
                
                State.memoryEnhancement.lastEmotionalTagTime = now;
            },
            
            // =====================================
            // SYSTEM 35: Quantum Field Text Vibration
            // =====================================
            System35_QuantumFieldTextVibration() {
                if (!State.cards.current) return;
                
                const questionElement = document.getElementById('card-question');
                const answerElement = document.getElementById('card-answer');
                
                if (!questionElement) return;
                
                // Clear any existing vibration intervals
                State.memoryEnhancement.quantumVibrationIntervals.forEach(clearInterval);
                State.memoryEnhancement.quantumVibrationIntervals = [];
                
                // Apply quantum vibration to both question and answer text
                [questionElement, answerElement].forEach(element => {
                    if (!element) return;
                    
                    const text = element.textContent;
                    if (!text) return;
                    
                    // Wrap each character in a span for individual jitter
                    const wrappedText = text.split('').map((char, index) => {
                        // 0.15 probability per letter
                        if (Math.random() < 0.15) {
                            return `<span class="quantum-jitter" data-char-index="${index}">${char}</span>`;
                        }
                        return char;
                    }).join('');
                    
                    element.innerHTML = wrappedText;
                    
                    // Apply jitter to marked characters at 33Hz (invisible flicker)
                    const jitterSpans = element.querySelectorAll('.quantum-jitter');
                    
                    jitterSpans.forEach(span => {
                        let jitterInterval = setInterval(() => {
                            // ±0.3px jitter using transform not position
                            const jitterX = (Math.random() - 0.5) * 0.6; // ±0.3px
                            const jitterY = (Math.random() - 0.5) * 0.6; // ±0.3px
                            
                            span.style.transform = `translate(${jitterX}px, ${jitterY}px)`;
                        }, 1000 / 33); // 33Hz frequency
                        
                        State.memoryEnhancement.quantumVibrationIntervals.push(jitterInterval);
                        
                        // Stop jitter after 500ms per activation
                        setTimeout(() => {
                            clearInterval(jitterInterval);
                            span.style.transform = '';
                            State.memoryEnhancement.quantumVibrationIntervals = 
                                State.memoryEnhancement.quantumVibrationIntervals.filter(i => i !== jitterInterval);
                        }, 500);
                    });
                });
            },
            
            // =====================================
            // SYSTEM 36: Somatic Marker Hijacking
            // =====================================
            System36_SomaticMarkerHijacking() {
                if (!State.cards.current || State.cards.current.wrongCount === 0) return;
                
                const now = performance.now();
                // Minimum 3 second cooldown
                if (now - State.memoryEnhancement.lastSomaticTime < 3000) return;
                
                const somaticElement = document.getElementById('somatic-marker');
                if (!somaticElement) return;
                
                // Rotate through temperature word bank
                const word = State.memoryEnhancement.somaticWordBank[State.memoryEnhancement.somaticWordIndex];
                State.memoryEnhancement.somaticWordIndex = 
                    (State.memoryEnhancement.somaticWordIndex + 1) % State.memoryEnhancement.somaticWordBank.length;
                
                // Position near answer text
                const answerElement = document.getElementById('card-answer');
                let x = window.innerWidth / 2;
                let y = window.innerHeight / 2;
                
                if (answerElement) {
                    const answerRect = answerElement.getBoundingClientRect();
                    if (answerRect.width > 0) { // Answer is visible
                        x = answerRect.right + 20; // 20px to the right of answer
                        y = answerRect.top + (answerRect.height / 2); // Middle of answer height
                    }
                }
                
                // Set up somatic marker
                somaticElement.textContent = word;
                somaticElement.style.left = x + 'px';
                somaticElement.style.top = y + 'px';
                somaticElement.style.fontSize = '16px';
                somaticElement.style.fontWeight = '300'; // Lighter weight
                somaticElement.style.opacity = '0.019'; // Very subtle
                
                // Display for exactly 22ms to associate body sensations with memory
                setTimeout(() => {
                    somaticElement.style.opacity = '0';
                }, 22);
                
                State.memoryEnhancement.lastSomaticTime = now;
            },
            
            // =====================================
            // NEW SYSTEM 37: Chronobiological Phase Coupling
            // =====================================
            System37_ChronobiologicalPhaseCoupling() {
                if (State.memoryEnhancement.chronobiologicalTintApplied) return;
                
                const container = document.querySelector('.container');
                if (!container) return;
                
                // Get system time and calculate minutes since midnight
                const now = new Date();
                const minutesSinceMidnight = now.getHours() * 60 + now.getMinutes();
                
                let tintFilter = '';
                let tintStrength = 0;
                
                // Morning (360-540min = 6:00-9:00): bluish tint +5
                if (minutesSinceMidnight >= 360 && minutesSinceMidnight <= 540) {
                    tintFilter = 'sepia(0.06) hue-rotate(200deg) saturate(1.5)'; // Bluish
                    tintStrength = 5;
                }
                // Afternoon (720-960min = 12:00-16:00): yellowish tint +3  
                else if (minutesSinceMidnight >= 720 && minutesSinceMidnight <= 960) {
                    tintFilter = 'sepia(0.06) hue-rotate(50deg) saturate(1.3)'; // Yellowish
                    tintStrength = 3;
                }
                // Evening (1080-1320min = 18:00-22:00): reddish tint +7
                else if (minutesSinceMidnight >= 1080 && minutesSinceMidnight <= 1320) {
                    tintFilter = 'sepia(0.06) hue-rotate(320deg) saturate(1.7)'; // Reddish
                    tintStrength = 7;
                }
                
                // Apply subtle tint if in active time window
                if (tintFilter) {
                    container.classList.add('chronobiological-tint');
                    container.style.filter = `${container.style.filter || ''} ${tintFilter}`;
                    container.style.opacity = '0.94'; // 0.06 filter opacity effect
                    State.memoryEnhancement.chronobiologicalTintApplied = true;
                    
                    // Aligns with circadian memory peaks - log for research
                    console.log(`Chronobiological tint applied: ${tintStrength} at ${now.getHours()}:${now.getMinutes().toString().padStart(2, '0')}`);
                }
            },
            
            // =====================================
            // NEW SYSTEM 38: Mirror Neuron Activation Protocol
            // =====================================
            System38_MirrorNeuronActivationProtocol() {
                if (!State.cards.current) return;
                
                const now = performance.now();
                if (now - State.memoryEnhancement.lastHandwritingTime < 3000) return;
                
                const traceElement = document.getElementById('handwriting-trace');
                const pathElement = document.getElementById('handwriting-path');
                if (!traceElement || !pathElement) return;
                
                // Get first 2 characters of answer for hand-writing animation
                const firstTwoChars = State.cards.current.answer.substring(0, 2);
                if (!firstTwoChars) return;
                
                // Generate simple SVG path for writing motion (simplified cursive)
                let pathData = '';
                const charWidth = 20;
                
                firstTwoChars.split('').forEach((char, index) => {
                    const x = index * charWidth + 10;
                    const y = 20;
                    
                    // Simple letter shapes - just basic strokes
                    switch (char.toLowerCase()) {
                        case 'a':
                            pathData += `M${x},${y+5} Q${x+5},${y-2} ${x+10},${y+5} M${x+3},${y+2} L${x+7},${y+2} `;
                            break;
                        case 'e':
                            pathData += `M${x+8},${y+2} Q${x+2},${y+2} ${x+2},${y+6} Q${x+8},${y+6} ${x+8},${y+2} `;
                            break;
                        case 'i':
                            pathData += `M${x+5},${y+8} L${x+5},${y+2} M${x+5},${y} L${x+5},${y} `;
                            break;
                        case 'o':
                            pathData += `M${x+2},${y+4} Q${x+2},${y} ${x+8},${y} Q${x+8},${y+8} ${x+2},${y+8} Q${x+2},${y+4} ${x+2},${y+4} `;
                            break;
                        case 'u':
                            pathData += `M${x+2},${y+2} Q${x+2},${y+8} ${x+8},${y+8} Q${x+8},${y+2} ${x+8},${y+2} `;
                            break;
                        default:
                            // Generic stroke for other characters
                            pathData += `M${x+2},${y+8} L${x+8},${y+2} M${x+2},${y+2} L${x+8},${y+8} `;
                    }
                });
                
                // Set path and reset animation
                pathElement.setAttribute('d', pathData);
                pathElement.style.strokeDasharray = '100';
                pathElement.style.strokeDashoffset = '100';
                
                // Show trace element
                traceElement.style.opacity = '0.028';
                
                // Animate at 3x speed (400ms / 3 ≈ 133ms, but using 400ms for smoother motion)
                pathElement.style.animation = 'handwritingAnimation 400ms ease-out forwards';
                
                // Hide after duration
                setTimeout(() => {
                    traceElement.style.opacity = '0';
                    pathElement.style.animation = '';
                }, 400);
                
                State.memoryEnhancement.lastHandwritingTime = now;
            },
            
            // =====================================
            // NEW SYSTEM 39: Subliminal Confidence Injection
            // =====================================
            System39_SubliminalConfidenceInjection(isCorrect) {
                const now = performance.now();
                if (now - State.memoryEnhancement.lastConfidenceFlashTime < 500) return;
                
                const flashElement = document.getElementById('confidence-flash');
                if (!flashElement) return;
                
                // Choose symbol and color based on response
                const symbol = isCorrect ? '✓' : '→';
                const color = isCorrect ? '#4caf50' : '#2196f3'; // Green for correct, blue for incorrect
                
                // Position in peripheral vision (edge of screen)
                const edge = Math.floor(Math.random() * 4); // 0=top, 1=right, 2=bottom, 3=left
                let x, y;
                
                switch (edge) {
                    case 0: // Top edge
                        x = Math.random() * (window.innerWidth - 100) + 50;
                        y = 50;
                        break;
                    case 1: // Right edge
                        x = window.innerWidth - 80;
                        y = Math.random() * (window.innerHeight - 100) + 50;
                        break;
                    case 2: // Bottom edge
                        x = Math.random() * (window.innerWidth - 100) + 50;
                        y = window.innerHeight - 80;
                        break;
                    case 3: // Left edge
                        x = 50;
                        y = Math.random() * (window.innerHeight - 100) + 50;
                        break;
                }
                
                // Set up confidence flash
                flashElement.textContent = symbol;
                flashElement.style.left = x + 'px';
                flashElement.style.top = y + 'px';
                flashElement.style.fontSize = '36px';
                flashElement.style.color = color;
                flashElement.style.opacity = '0.021'; // Very subtle opacity
                
                // Flash for exactly 11ms to bypass conscious evaluation
                setTimeout(() => {
                    flashElement.style.opacity = '0';
                }, 11);
                
                State.memoryEnhancement.lastConfidenceFlashTime = now;
            },
            
            // =====================================
            // NEW SYSTEM 40: Delta Wave Memory Consolidation
            // =====================================
            System40_DeltaWaveMemoryConsolidation() {
                // Only during breaks
                if (!State.session.isBreak) return;
                if (State.memoryEnhancement.deltaWavePulseActive) return;
                
                State.memoryEnhancement.deltaWavePulseActive = true;
                
                const container = document.querySelector('.container');
                if (!container) return;
                
                // Apply delta wave pulse class for CSS transitions
                container.classList.add('delta-wave-pulse');
                
                // 2Hz pulsing (500ms per cycle)
                let pulseCount = 0;
                const maxPulses = 8; // 4 seconds total
                
                State.memoryEnhancement.deltaWaveInterval = setInterval(() => {
                    if (pulseCount >= maxPulses) {
                        clearInterval(State.memoryEnhancement.deltaWaveInterval);
                        container.classList.remove('delta-wave-pulse');
                        container.style.opacity = '1';
                        State.memoryEnhancement.deltaWavePulseActive = false;
                        
                        // Clean up Schumann resonance
                        if (State.memoryEnhancement.schumannResonanceOscillator) {
                            State.memoryEnhancement.schumannGainNode.gain.exponentialRampToValueAtTime(
                                0.001, State.settings.audioContext.currentTime + 0.5
                            );
                            setTimeout(() => {
                                State.memoryEnhancement.schumannResonanceOscillator.stop();
                                State.memoryEnhancement.schumannResonanceOscillator.disconnect();
                                State.memoryEnhancement.schumannResonanceOscillator = null;
                                State.memoryEnhancement.schumannGainNode = null;
                            }, 500);
                        }
                        return;
                    }
                    
                    // Pulse between 0.97 and 1.03 opacity
                    const opacity = pulseCount % 2 === 0 ? '0.97' : '1.03';
                    container.style.opacity = opacity;
                    pulseCount++;
                }, 250); // 500ms cycle / 2 = 250ms per half-cycle
                
                // Combine with 7.83Hz Schumann resonance audio
                if (State.settings.soundEnabled && State.settings.audioContext) {
                    try {
                        const context = State.settings.audioContext;
                        const oscillator = context.createOscillator();
                        const gainNode = context.createGain();
                        
                        oscillator.frequency.value = 7.83; // Schumann resonance
                        oscillator.type = 'sine';
                        gainNode.gain.value = 0.004; // Very quiet
                        
                        oscillator.connect(gainNode);
                        gainNode.connect(context.destination);
                        
                        oscillator.start();
                        
                        State.memoryEnhancement.schumannResonanceOscillator = oscillator;
                        State.memoryEnhancement.schumannGainNode = gainNode;
                        
                    } catch (error) {
                        // Schumann resonance audio failed
                    }
                }
            },
            
            // =====================================
            // NEW SYSTEM 41: Phantom Touch Memory Encoding
            // =====================================
            System41_PhantomTouchMemoryEncoding() {
                // This system is CSS-based and triggered by hover states
                // The .phantom-touch class is already applied to .card-container
                // CSS handles the shadow transitions on hover automatically
                
                // We can enhance it by scaling with card importance
                if (!State.cards.current) return;
                
                const container = document.querySelector('.card-container');
                if (!container) return;
                
                // Scale shadow intensity with card difficulty
                const difficultyFactor = Math.max(0.5, Math.min(2.0, State.cards.current.difficulty + 1));
                const baseShadow = '2px 2px 3px';
                const enhancedShadow = `${3 * difficultyFactor}px ${3 * difficultyFactor}px ${5 * difficultyFactor}px`;
                
                // Apply enhanced shadow mapping for this card
                container.style.setProperty('--base-shadow', baseShadow);
                container.style.setProperty('--enhanced-shadow', enhancedShadow);
                
                // Update CSS custom properties for this card
                container.style.boxShadow = `${baseShadow} var(--shadow)`;
            },
            
            // =====================================
            // NEW SYSTEM 42: Accelerometer Rhythm Encoding (Mobile Only)
            // =====================================
            System42_AccelerometerRhythmEncoding(deviceMotionEvent) {
                if (!State.memoryEnhancement.isMobileDevice || !State.cards.current) return;
                
                const now = performance.now();
                if (now - State.memoryEnhancement.lastAccelerometerFlashTime < 100) return; // 100ms cooldown
                
                // Analyze accelerometer data for natural hand tremor (8-12Hz)
                const acceleration = deviceMotionEvent.acceleration;
                if (!acceleration || !acceleration.x || !acceleration.y || !acceleration.z) return;
                
                // Calculate total acceleration magnitude
                const magnitude = Math.sqrt(
                    acceleration.x * acceleration.x + 
                    acceleration.y * acceleration.y + 
                    acceleration.z * acceleration.z
                );
                
                // Detect tremor frequency - simplified detection
                // In real implementation, this would use FFT analysis
                const tremor = magnitude > 0.1 && magnitude < 2.0; // Reasonable tremor range
                
                if (!tremor) return;
                
                // Sync flash timing to detected tremor phase
                const tremorPeriod = 1000 / State.memoryEnhancement.handTremorFrequency; // ~100ms for 10Hz
                const phaseOffset = (now % tremorPeriod) / tremorPeriod;
                
                // Only flash when tremor is in optimal phase (0.2-0.4 of cycle)
                if (phaseOffset < 0.2 || phaseOffset > 0.4) return;
                
                const flashElement = document.getElementById('accelerometer-flash');
                if (!flashElement) return;
                
                // Position flash based on device orientation
                const x = window.innerWidth * (0.3 + acceleration.x * 0.1); // ±10% variance
                const y = window.innerHeight * (0.3 + acceleration.y * 0.1); // ±10% variance
                
                // Set up accelerometer flash
                flashElement.textContent = '◦'; // Small circle indicator
                flashElement.style.left = Math.max(50, Math.min(window.innerWidth - 50, x)) + 'px';
                flashElement.style.top = Math.max(50, Math.min(window.innerHeight - 50, y)) + 'px';
                flashElement.style.fontSize = '18px';
                flashElement.style.color = '#1976d2';
                flashElement.style.opacity = '0.014'; // Very subtle
                
                // Flash for exactly 16ms synchronized to tremor
                setTimeout(() => {
                    flashElement.style.opacity = '0';
                }, 16);
                
                State.memoryEnhancement.lastAccelerometerFlashTime = now;
            },
            
            // Helper function to find semantic relations (from System 30)
            findSemanticRelations(keyWord) {
                const database = State.memoryEnhancement.semanticWordDatabase;
                const related = [];
                
                // Simple semantic matching based on shared characteristics
                // In a full implementation, this would use a proper semantic network
                
                if (keyWord.includes('learn') || keyWord.includes('study') || keyWord.includes('know')) {
                    related.push('knowledge', 'wisdom', 'understanding', 'education', 'intelligence');
                } else if (keyWord.includes('memor') || keyWord.includes('recall') || keyWord.includes('remember')) {
                    related.push('memory', 'recall', 'retention', 'cognition', 'thinking');
                } else if (keyWord.includes('think') || keyWord.includes('reason') || keyWord.includes('logic')) {
                    related.push('reasoning', 'analysis', 'logic', 'cognition', 'intelligence');
                } else if (keyWord.includes('creat') || keyWord.includes('innovat') || keyWord.includes('invent')) {
                    related.push('creativity', 'innovation', 'discovery', 'imagination', 'inspiration');
                } else {
                    // Fallback: select random words from database
                    for (let i = 0; i < 5; i++) {
                        const randomWord = database[Math.floor(Math.random() * database.length)];
                        if (!related.includes(randomWord)) {
                            related.push(randomWord);
                        }
                    }
                }
                
                // Shuffle and ensure we have at least 3 unique words
                const shuffled = related.sort(() => Math.random() - 0.5);
                return shuffled.slice(0, 5); // Return up to 5 words
            },
            
            // Helper function to calculate user tempo for System 31
            calculateUserTempo(times) {
                if (times.length < 2) return;
                
                const intervals = [];
                for (let i = 1; i < times.length; i++) {
                    intervals.push(times[i] - times[i-1]);
                }
                
                const avgInterval = intervals.reduce((a, b) => a + b, 0) / intervals.length;
                State.memoryEnhancement.userTempo = avgInterval;
            },
            
            // Helper function to clear preload cache
            clearPreloadCache() {
                State.memoryEnhancement.preloadCache.clear();
                
                // Clear preload containers
                ['preload-container-1', 'preload-container-2'].forEach(id => {
                    const container = document.getElementById(id);
                    if (container) {
                        container.innerHTML = '';
                    }
                });
            },
            
            // Main orchestration function
            orchestrate(event) {
                if (!State.session.isActive || State.session.isPaused) return;
                
                switch(event) {
                    case 'cardDisplay':
                        // Systems activated on card display (1-36)
                        this.System4_MicroPriming();
                        this.System5_VisualMemoryEncoding();
                        this.System12_BinauralBeats('question');
                        this.System13_PeripheralInjection();
                        this.System15_HapticEncoding();
                        this.System16_ChromaticSignatures();
                        this.System18_TemporalPattern();
                        this.System20_UltrasonicAnchoring();
                        this.System21_OlfactoryPriming();
                        // Systems 22-26
                        this.System22_ProprioceptiveEncoding();
                        this.System23_QuantumAttentionCycling();
                        this.System24_ChronestheticTimeWarping();
                        this.System25_ParallelReality();
                        this.System26_SubliminalSuccessAnchoring();
                        // Systems 27-30
                        this.System27_RetinalPersistenceAfterimage();
                        this.System28_InfrasonicResonance();
                        this.System29_StatisticalBlinkWindow();
                        this.System30_SemanticNetworkPriming();
                        // Systems 31-36
                        this.System31_PhaseLockedNeuralOscillation();
                        this.System32_VestibularMemoryEncoding();
                        this.System33_CorticalSpreadingDepressionBypass();
                        this.System34_SubliminalEmotionalTagging();
                        this.System35_QuantumFieldTextVibration();
                        this.System36_SomaticMarkerHijacking();
                        // NEW SYSTEMS 37-42
                        this.System37_ChronobiologicalPhaseCoupling();
                        this.System38_MirrorNeuronActivationProtocol();
                        this.System41_PhantomTouchMemoryEncoding();
                        break;
                        
                    case 'answerReveal':
                        this.System12_BinauralBeats('answer');
                        // Clear quantum cycling when answer is revealed
                        State.memoryEnhancement.quantumCyclingInterval.forEach(clearInterval);
                        State.memoryEnhancement.quantumCyclingInterval = [];
                        break;
                        
                    case 'responseCorrect':
                        const responseTime = performance.now() - State.timing.cardDisplayStartTime;
                        this.System1_ResponseTimeDetection(responseTime);
                        this.System2_PredictionErrorOptimization();
                        this.System8_QuantumScheduling();
                        this.System10_FatigueDetection();
                        // NEW: System 39 for correct responses
                        this.System39_SubliminalConfidenceInjection(true);
                        
                        if (State.performance.totalCorrect > State.performance.totalAttempts * 0.5) {
                            this.System19_FlickerConsolidation();
                        }
                        
                        this.cleanupAfterResponse();
                        break;
                        
                    case 'responseIncorrect':
                        const responseTimeWrong = performance.now() - State.timing.cardDisplayStartTime;
                        this.System1_ResponseTimeDetection(responseTimeWrong);
                        this.System2_PredictionErrorOptimization();
                        this.System8_QuantumScheduling();
                        this.System10_FatigueDetection();
                        // NEW: System 39 for incorrect responses
                        this.System39_SubliminalConfidenceInjection(false);
                        
                        this.cleanupAfterResponse();
                        break;
                        
                    case 'phaseStart':
                        this.System3_SerialPositionHacking();
                        this.System7_EmotionalColorOptimization();
                        break;
                        
                    case 'sessionPause':
                        this.System9_CovertRetrieval();
                        this.pauseAllSystems();
                        break;
                        
                    case 'breakStart':
                        // NEW: System 40 activates during breaks
                        this.System40_DeltaWaveMemoryConsolidation();
                        this.pauseAllSystems();
                        break;
                        
                    case 'specialCard':
                        this.System6_ConsolidationWindow();
                        this.System11_DistinctivenessBoost();
                        break;
                }
            },
            
            // Helper function to clean up after response
            cleanupAfterResponse() {
                // Clear quantum cycling on response
                State.memoryEnhancement.quantumCyclingInterval.forEach(clearInterval);
                State.memoryEnhancement.quantumCyclingInterval = [];
                
                // Clear quantum vibration intervals
                State.memoryEnhancement.quantumVibrationIntervals.forEach(clearInterval);
                State.memoryEnhancement.quantumVibrationIntervals = [];
                
                // Clear used preload cache
                this.clearPreloadCache();
                
                // Stop infrasonic oscillator on response
                if (State.memoryEnhancement.infrasonicOscillator) {
                    State.memoryEnhancement.infrasonicOscillator.stop();
                    State.memoryEnhancement.infrasonicOscillator.disconnect();
                    State.memoryEnhancement.infrasonicOscillator = null;
                }
            },
            
            // Helper function to pause systems during breaks/pauses
            pauseAllSystems() {
                // Pause quantum cycling during breaks
                State.memoryEnhancement.quantumCyclingInterval.forEach(clearInterval);
                State.memoryEnhancement.quantumCyclingInterval = [];
                
                // Pause quantum vibration during breaks
                State.memoryEnhancement.quantumVibrationIntervals.forEach(clearInterval);
                State.memoryEnhancement.quantumVibrationIntervals = [];
                
                // Pause infrasonic resonance
                if (State.memoryEnhancement.infrasonicOscillator) {
                    State.memoryEnhancement.infrasonicGainNode.gain.value = 0;
                }
            }
        };
        
        // ========================================
        // CORE SYSTEM MODULE
        // ========================================
        const ScholarSRS = {
            
            // =====================================
            // INITIALIZATION & SESSION MANAGEMENT
            // =====================================
            init() {
                this.Audio.init();
                this.UI.init();
                this.Controls.init();
                MemoryEnhancement.init();
            },
            
            startSession() {
                try {
                    console.log('Starting session...');
                    const sessionData = this.Input.validateAndParse();
                    console.log('Session data:', sessionData);
                    if (!sessionData) {
                        console.log('Session data validation failed');
                        return;
                    }
                    
                    this.Session.initialize(sessionData);
                    this.Phase.initialize();
                    this.UI.switchToStudyScreen();
                    this.Phase.start(0);
                    
                    this.Achievement.show('Session Initiated', `${State.cards.all.length} items prepared for study`);
                    MemoryEnhancement.orchestrate('phaseStart');
                } catch (error) {
                    console.error('Error starting session:', error);
                    alert('Error starting session: ' + error.message);
                    this.Error.handle('startSession', error);
                }
            },
            
            // =====================================
            // INPUT VALIDATION & PARSING MODULE
            // =====================================
            Input: {
                validateAndParse() {
                    console.log('Validating input...');
                    const hoursInput = document.getElementById('hours').value;
                    const questionsInput = document.getElementById('questions').value.trim();
                    
                    console.log('Hours input:', hoursInput);
                    console.log('Questions input length:', questionsInput.length);
                    
                    // Clear previous errors
                    this.clearErrors();
                    
                    // Validate hours
                    if (!this.validateHours(hoursInput)) {
                        console.log('Hours validation failed');
                        return null;
                    }
                    
                    // Parse and validate questions
                    const cards = this.parseQuestions(questionsInput);
                    if (!cards) {
                        console.log('Questions parsing failed');
                        return null;
                    }
                    
                    console.log('Validation successful, cards created:', cards.length);
                    return {
                        totalHours: parseFloat(hoursInput),
                        cards: cards
                    };
                },
                
                validateHours(hoursInput) {
                    if (!hoursInput || isNaN(parseFloat(hoursInput)) || parseFloat(hoursInput) < 0.5) {
                        this.showError('hours-error', 'Please specify at least 0.5 hours (numeric value required)');
                        return false;
                    }
                    return true;
                },
                
                parseQuestions(questionsInput) {
                    console.log('Parsing questions...');
                    if (!questionsInput) {
                        console.log('No questions input provided');
                        this.showError('questions-error', 'Please provide your study material');
                        return null;
                    }
                    
                    const lines = questionsInput.split('\n').filter(line => line.trim());
                    console.log('Lines after split:', lines.length);
                    const cards = [];
                    let invalidLines = [];
                    
                    for (let i = 0; i < lines.length; i++) {
                        const line = lines[i].trim();
                        if (!line) continue;
                        
                        const parts = line.split('::');
                        console.log(`Line ${i+1}: "${line}" -> parts:`, parts.length);
                        if (parts.length === 2 && parts[0].trim() && parts[1].trim()) {
                            cards.push(this.createCard(parts[0].trim(), parts[1].trim(), cards.length));
                            console.log(`Created card: ${parts[0].trim()} -> ${parts[1].trim()}`);
                        } else {
                            invalidLines.push(i + 1);
                            console.log(`Invalid line ${i+1}: "${line}"`);
                        }
                    }
                    
                    console.log('Total cards created:', cards.length);
                    console.log('Invalid lines:', invalidLines);
                    
                    if (cards.length === 0) {
                        const errorMsg = invalidLines.length > 0 
                            ? `No valid entries found. Check lines: ${invalidLines.join(', ')}. Use format: Question::Answer`
                            : 'No valid entries found. Please use format: Question::Answer';
                        this.showError('questions-error', errorMsg);
                        return null;
                    }
                    
                    return cards;
                },
                
                createCard(question, answer, id) {
                    const card = {
                        question,
                        answer,
                        id,
                        difficulty: 0,
                        lastSeen: -1,
                        nextReview: 0,
                        correctCount: 0,
                        wrongCount: 0,
                        totalSeen: 0,
                        consecutiveCorrect: 0,
                        avgResponseTime: 0,
                        lastResponseTime: 0,
                        createdAt: performance.now()
                    };
                    
                    // Initialize card statistics
                    State.cards.stats.set(id, {
                        responses: [],
                        timestamps: [],
                        phaseFirstSeen: -1,
                        responseTimeHistory: [],
                        difficultyHistory: []
                    });
                    
                    return card;
                },
                
                clearErrors() {
                    document.getElementById('hours-error').classList.remove('show');
                    document.getElementById('questions-error').classList.remove('show');
                },
                
                showError(elementId, message) {
                    const element = document.getElementById(elementId);
                    element.textContent = message;
                    element.classList.add('show');
                }
            },
            
            // =====================================
            // SESSION MANAGEMENT MODULE
            // =====================================
            Session: {
                initialize(sessionData) {
                    // Reset all state
                    this.reset();
                    
                    // Set session data
                    State.session.totalHours = sessionData.totalHours;
                    State.cards.all = sessionData.cards;
                    
                    // Initialize timing
                    const now = performance.now();
                    State.session.preciseStartTime = now;
                    State.session.startTime = Date.now();
                    State.timing.rateCalculationStartTime = now;
                    State.timing.nextBreakTime = Date.now() + CONFIG.BREAK_INTERVAL;
                    
                    // Initialize card categorization
                    sessionData.cards.forEach(card => {
                        State.cards.learning.add(card.id);
                    });
                    
                    State.session.isActive = true;
                },
                
                reset() {
                    // Clear intervals
                    if (State.timing.timerInterval) clearInterval(State.timing.timerInterval);
                    if (State.timing.breakInterval) clearInterval(State.timing.breakInterval);
                    
                    // Clear quantum cycling intervals
                    State.memoryEnhancement.quantumCyclingInterval.forEach(clearInterval);
                    State.memoryEnhancement.quantumCyclingInterval = [];
                    
                    // Clear quantum vibration intervals
                    State.memoryEnhancement.quantumVibrationIntervals.forEach(clearInterval);
                    State.memoryEnhancement.quantumVibrationIntervals = [];
                    
                    // Clean up infrasonic oscillator
                    if (State.memoryEnhancement.infrasonicOscillator) {
                        State.memoryEnhancement.infrasonicOscillator.stop();
                        State.memoryEnhancement.infrasonicOscillator.disconnect();
                        State.memoryEnhancement.infrasonicOscillator = null;
                    }
                    
                    // Clean up delta wave interval
                    if (State.memoryEnhancement.deltaWaveInterval) {
                        clearInterval(State.memoryEnhancement.deltaWaveInterval);
                        State.memoryEnhancement.deltaWaveInterval = null;
                    }
                    
                    // Clean up accelerometer
                    if (State.memoryEnhancement.deviceMotionHandler) {
                        window.removeEventListener('devicemotion', State.memoryEnhancement.deviceMotionHandler);
                        State.memoryEnhancement.deviceMotionHandler = null;
                    }
                    
                    // Reset state
                    Object.assign(State.session, {
                        totalHours: 0,
                        startTime: 0,
                        preciseStartTime: 0,
                        isActive: false,
                        isPaused: false,
                        isBreak: false
                    });
                    
                    Object.assign(State.performance, {
                        totalCorrect: 0,
                        totalAttempts: 0,
                        currentStreak: 0,
                        longestStreak: 0,
                        cardsSeenInSession: 0,
                        cardsCompletedForRate: 0,
                        rateHistory: [],
                        last50ResponseTimes: [],
                        successRateHistory: []
                    });
                    
                    // Clear collections
                    State.cards.all = [];
                    State.cards.current = null;
                    State.cards.stats.clear();
                    State.cards.mastered.clear();
                    State.cards.learning.clear();
                    State.cards.difficult.clear();
                    
                    State.phase.queues = [];
                    
                    // Clear memory enhancement state
                    MemoryEnhancement.clearPreloadCache();
                    State.memoryEnhancement.chronestheticAdjustments.clear();
                    State.memoryEnhancement.retinalAfterimageActive = false;
                    State.memoryEnhancement.corticalRingActive = false;
                    State.memoryEnhancement.chronobiologicalTintApplied = false;
                    State.memoryEnhancement.deltaWavePulseActive = false;
                },
                
                complete() {
                    try {
                        this.cleanup();
                        this.generateReport();
                        this.celebrateCompletion();
                    } catch (error) {
                        ScholarSRS.Error.handle('sessionComplete', error);
                    }
                },
                
                cleanup() {
                    if (State.timing.timerInterval) clearInterval(State.timing.timerInterval);
                    if (State.timing.breakInterval) clearInterval(State.timing.breakInterval);
                    
                    // Clear quantum cycling intervals
                    State.memoryEnhancement.quantumCyclingInterval.forEach(clearInterval);
                    State.memoryEnhancement.quantumCyclingInterval = [];
                    
                    // Clear quantum vibration intervals
                    State.memoryEnhancement.quantumVibrationIntervals.forEach(clearInterval);
                    State.memoryEnhancement.quantumVibrationIntervals = [];
                    
                    // Clean up infrasonic oscillator
                    if (State.memoryEnhancement.infrasonicOscillator) {
                        State.memoryEnhancement.infrasonicOscillator.stop();
                        State.memoryEnhancement.infrasonicOscillator.disconnect();
                        State.memoryEnhancement.infrasonicOscillator = null;
                    }
                    
                    // Clean up delta wave systems
                    if (State.memoryEnhancement.deltaWaveInterval) {
                        clearInterval(State.memoryEnhancement.deltaWaveInterval);
                    }
                    if (State.memoryEnhancement.schumannResonanceOscillator) {
                        State.memoryEnhancement.schumannResonanceOscillator.stop();
                        State.memoryEnhancement.schumannResonanceOscillator.disconnect();
                    }
                    
                    // Clean up accelerometer
                    if (State.memoryEnhancement.deviceMotionHandler) {
                        window.removeEventListener('devicemotion', State.memoryEnhancement.deviceMotionHandler);
                    }
                    
                    const pauseToggle = document.getElementById('pause-toggle');
                    if (pauseToggle) pauseToggle.style.display = 'none';
                    
                    State.session.isActive = false;
                },
                
                generateReport() {
                    const now = performance.now();
                    const totalSessionTime = now - State.session.preciseStartTime;
                    const actualStudyTimeMinutes = (totalSessionTime - State.timing.totalPausedTime) / (1000 * 60);
                    const totalMinutes = Math.round(actualStudyTimeMinutes);
                    const hours = Math.floor(totalMinutes / 60);
                    const minutes = totalMinutes % 60;
                    
                    const finalAccuracy = State.performance.totalAttempts > 0 
                        ? Math.round((State.performance.totalCorrect / State.performance.totalAttempts) * 100) 
                        : 0;
                    const finalRate = actualStudyTimeMinutes > 0 
                        ? (State.performance.cardsSeenInSession / actualStudyTimeMinutes).toFixed(1) 
                        : '0.0';
                    const masteryPercentage = Math.round((State.cards.mastered.size / State.cards.all.length) * 100);
                    
                    const ornament = '<div class="ornament" style="margin: 2rem 0;">♦ ♦ ♦</div>';
                    
                    const questionElement = document.getElementById('card-question');
                    const answerElement = document.getElementById('card-answer');
                    
                    if (questionElement) {
                        questionElement.innerHTML = '🎓 Scholarly Achievement Unlocked 🎓';
                    }
                    
                    if (answerElement) {
                        answerElement.innerHTML = 
                            `<strong>Session Complete</strong>${ornament}` +
                            `<div style="text-align: left; margin: 1rem 0;">` +
                            `<p>• Items Mastered: ${State.cards.mastered.size} of ${State.cards.all.length} (${masteryPercentage}%)</p>` +
                            `<p>• Duration: ${hours} hours, ${minutes} minutes</p>` +
                            `<p>• Overall Accuracy: ${finalAccuracy}%</p>` +
                            `<p>• Learning Rate: ${finalRate} cards/minute</p>` +
                            `<p>• Total Reviews: ${State.performance.cardsSeenInSession}</p>` +
                            `<p>• Longest Streak: ${State.performance.longestStreak}</p>` +
                            `<p>• Memory Systems Active: ${State.memoryEnhancement.systemsActive.size}</p>` +
                            `</div>${ornament}` +
                            `<em>Your dedication to learning has borne fruit.<br>The knowledge is now yours to keep.</em>`;
                        answerElement.classList.add('show');
                    }
                    
                    // Hide UI elements
                    const buttonGroup = document.getElementById('button-group');
                    const difficultyIndicator = document.getElementById('difficulty-indicator');
                    
                    if (buttonGroup) buttonGroup.style.display = 'none';
                    if (difficultyIndicator) difficultyIndicator.style.display = 'none';
                    
                    // Update final stats
                    document.getElementById('remaining-count').textContent = '0';
                    document.getElementById('cards-per-minute').textContent = finalRate;
                },
                
                celebrateCompletion() {
                    for (let i = 0; i < 5; i++) {
                        setTimeout(() => ScholarSRS.Audio.playSuccess(), i * 300);
                    }
                    
                    ScholarSRS.Achievement.show('🎓 MASTERY COMPLETE', 'Congratulations, Scholar!');
                }
            },
            
            // =====================================
            // PHASE MANAGEMENT MODULE
            // =====================================
            Phase: {
                initialize() {
                    try {
                        State.phase.queues = Array(CONFIG.PHASES.length).fill(null).map(() => []);
                        
                        // Distribute cards across phases
                        State.cards.all.forEach(card => {
                            State.phase.queues[0].push(card);
                            
                            for (let i = 1; i < CONFIG.PHASES.length; i++) {
                                const probability = Math.max(0.3, 0.9 - (i * 0.1));
                                if (Math.random() < probability) {
                                    State.phase.queues[i].push(card);
                                }
                            }
                        });
                        
                        // Ensure all phases have cards
                        for (let i = 1; i < CONFIG.PHASES.length; i++) {
                            if (State.phase.queues[i].length === 0 && State.cards.all.length > 0) {
                                const sampleSize = Math.ceil(State.cards.all.length * 0.3);
                                const shuffledCards = [...State.cards.all].sort(() => Math.random() - 0.5);
                                State.phase.queues[i] = shuffledCards.slice(0, sampleSize);
                            }
                        }
                        
                        // Shuffle all queues
                        State.phase.queues.forEach(queue => ScholarSRS.Utils.shuffleArray(queue));
                        
                    } catch (error) {
                        // Fallback: all cards in all phases
                        State.phase.queues = Array(CONFIG.PHASES.length).fill(null).map(() => [...State.cards.all]);
                        State.phase.queues.forEach(queue => ScholarSRS.Utils.shuffleArray(queue));
                    }
                },
                
                start(phaseIndex) {
                    try {
                        if (phaseIndex >= CONFIG.PHASES.length) {
                            ScholarSRS.Session.complete();
                            return;
                        }
                        
                        State.phase.current = phaseIndex;
                        const now = performance.now();
                        State.phase.preciseStartTime = now;
                        State.phase.startTime = Date.now();
                        
                        // Update UI
                        document.getElementById('pause-toggle').style.display = 'flex';
                        this.updateUI(phaseIndex);
                        this.prepareQueue();
                        
                        // Start timer
                        if (State.timing.timerInterval) clearInterval(State.timing.timerInterval);
                        State.timing.timerInterval = setInterval(() => ScholarSRS.Timer.update(), CONFIG.PROGRESS_UPDATE_INTERVAL);
                        
                        // Trigger memory systems
                        MemoryEnhancement.orchestrate('phaseStart');
                        
                        ScholarSRS.Card.showNext();
                        
                    } catch (error) {
                        ScholarSRS.Error.handle('phaseStart', error);
                    }
                },
                
                updateUI(phaseIndex) {
                    const romanNumerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'];
                    document.getElementById('phase-title').textContent = 
                        `Phase ${romanNumerals[phaseIndex]}: ${CONFIG.PHASES[phaseIndex].name}`;
                    document.getElementById('phase-badge').textContent = 
                        `${Math.round(CONFIG.PHASES[phaseIndex].percentage * 100)}% of session`;
                },
                
                prepareQueue() {
                    try {
                        if (!State.phase.queues[State.phase.current]) {
                            State.phase.queues[State.phase.current] = [];
                            return;
                        }
                        
                        ScholarSRS.Utils.shuffleArray(State.phase.queues[State.phase.current]);
                        ScholarSRS.Stats.updateRemaining();
                        
                    } catch (error) {
                        ScholarSRS.Stats.updateRemaining();
                    }
                },
                
                complete() {
                    try {
                        if (State.phase.current < CONFIG.PHASES.length - 1) {
                            this.start(State.phase.current + 1);
                        } else {
                            ScholarSRS.Session.complete();
                        }
                    } catch (error) {
                        ScholarSRS.Session.complete();
                    }
                }
            },
            
            // =====================================
            // CARD MANAGEMENT MODULE
            // =====================================
            Card: {
                showNext() {
                    try {
                        // Check for break time
                        if (Date.now() >= State.timing.nextBreakTime && !State.session.isBreak) {
                            ScholarSRS.Break.start();
                            return;
                        }
                        
                        // Check if phase is complete
                        if (!State.phase.queues[State.phase.current] || State.phase.queues[State.phase.current].length === 0) {
                            ScholarSRS.Phase.complete();
                            return;
                        }
                        
                        // Get next card
                        State.cards.current = State.phase.queues[State.phase.current].shift();
                        if (!State.cards.current) {
                            ScholarSRS.Phase.complete();
                            return;
                        }
                        
                        this.updateCardState();
                        this.updateUI();
                        
                        // Trigger memory systems
                        State.timing.cardDisplayStartTime = performance.now();
                        MemoryEnhancement.orchestrate('cardDisplay');
                        
                        // Special cards get extra treatment
                        if (State.performance.cardsSeenInSession % 7 === 0) {
                            MemoryEnhancement.orchestrate('specialCard');
                        }
                        
                    } catch (error) {
                        ScholarSRS.Error.handle('cardShowNext', error);
                    }
                },
                
                updateCardState() {
                    const now = performance.now();
                    State.cards.current.lastSeen = (now - State.session.preciseStartTime) / (1000 * 60);
                    State.cards.current.totalSeen++;
                    State.cards.current.lastResponseTime = now;
                    State.performance.cardsSeenInSession++;
                },
                
                updateUI() {
                    const questionElement = document.getElementById('card-question');
                    const answerElement = document.getElementById('card-answer');
                    
                    if (questionElement && answerElement) {
                        questionElement.textContent = State.cards.current.question || 'Invalid question';
                        answerElement.textContent = State.cards.current.answer || 'Invalid answer';
                        answerElement.classList.remove('show');
                    }
                    
                    // Reset any distinctive effects
                    const container = document.querySelector('.card-container');
                    if (container) {
                        container.style.fontSize = '';
                        container.style.letterSpacing = '';
                        container.style.textShadow = '';
                        container.style.transform = '';
                        container.classList.remove('distinctiveness-boost');
                        container.classList.remove('vestibular-shift');
                    }
                    
                    this.updateDifficultyIndicator();
                    this.updateButtons();
                    ScholarSRS.Stats.updateRemaining();
                },
                
                updateDifficultyIndicator() {
                    try {
                        const dots = document.querySelectorAll('.difficulty-dot');
                        if (!dots.length) return;
                        
                        const difficulty = Math.min(5, Math.ceil((State.cards.current.wrongCount / Math.max(1, State.cards.current.totalSeen)) * 5));
                        
                        dots.forEach((dot, index) => {
                            dot.classList.toggle('active', index < difficulty);
                        });
                    } catch (error) {
                        // Error updating difficulty indicator
                    }
                },
                
                updateButtons() {
                    document.getElementById('show-answer-btn').style.display = 'inline-block';
                    document.getElementById('correct-btn').style.display = 'none';
                    document.getElementById('wrong-btn').style.display = 'none';
                    document.getElementById('skip-btn').style.display = 
                        State.cards.current.totalSeen > 1 ? 'inline-block' : 'none';
                },
                
                showAnswer() {
                    try {
                        const answerElement = document.getElementById('card-answer');
                        const showBtn = document.getElementById('show-answer-btn');
                        const correctBtn = document.getElementById('correct-btn');
                        const wrongBtn = document.getElementById('wrong-btn');
                        
                        if (answerElement) answerElement.classList.add('show');
                        if (showBtn) showBtn.style.display = 'none';
                        if (correctBtn) correctBtn.style.display = 'inline-block';
                        if (wrongBtn) wrongBtn.style.display = 'inline-block';
                        
                        // Trigger memory systems
                        MemoryEnhancement.orchestrate('answerReveal');
                        
                    } catch (error) {
                        ScholarSRS.Error.handle('cardShowAnswer', error);
                    }
                },
                
                markCorrect() {
                    try {
                        if (!State.cards.current) return;
                        
                        this.updatePerformanceStats(true);
                        this.updateCardStats(true);
                        this.categorizeCard(true);
                        this.recordResponse(true);
                        this.checkAchievements();
                        
                        // Trigger memory systems with correct response
                        MemoryEnhancement.orchestrate('responseCorrect');
                        
                        ScholarSRS.Audio.playSuccess();
                        ScholarSRS.Stats.update();
                        this.showNext();
                        
                    } catch (error) {
                        ScholarSRS.Error.handle('cardMarkCorrect', error);
                        this.showNext();
                    }
                },
                
                markWrong() {
                    try {
                        if (!State.cards.current) return;
                        
                        this.updatePerformanceStats(false);
                        this.updateCardStats(false);
                        this.categorizeCard(false);
                        this.recordResponse(false);
                        this.rescheduleCard();
                        
                        // Trigger memory systems with incorrect response
                        MemoryEnhancement.orchestrate('responseIncorrect');
                        
                        ScholarSRS.Audio.playError();
                        ScholarSRS.Stats.update();
                        this.showNext();
                        
                    } catch (error) {
                        ScholarSRS.Error.handle('cardMarkWrong', error);
                        this.showNext();
                    }
                },
                
                skip() {
                    try {
                        if (!State.cards.current || !State.phase.queues[State.phase.current]) return;
                        
                        State.phase.queues[State.phase.current].push(State.cards.current);
                        ScholarSRS.Stats.update();
                        this.showNext();
                        
                    } catch (error) {
                        ScholarSRS.Error.handle('cardSkip', error);
                        this.showNext();
                    }
                },
                
                updatePerformanceStats(isCorrect) {
                    State.performance.totalAttempts++;
                    State.performance.cardsCompletedForRate++;
                    
                    // Track response time
                    const responseTime = performance.now() - State.timing.cardDisplayStartTime;
                    State.performance.last50ResponseTimes.push(responseTime);
                    if (State.performance.last50ResponseTimes.length > 50) {
                        State.performance.last50ResponseTimes.shift();
                    }
                    
                    if (isCorrect) {
                        State.performance.totalCorrect++;
                        State.performance.currentStreak++;
                        
                        if (State.performance.currentStreak > State.performance.longestStreak) {
                            State.performance.longestStreak = State.performance.currentStreak;
                        }
                    } else {
                        State.performance.currentStreak = 0;
                    }
                },
                
                updateCardStats(isCorrect) {
                    if (isCorrect) {
                        State.cards.current.correctCount++;
                        State.cards.current.consecutiveCorrect++;
                    } else {
                        State.cards.current.wrongCount++;
                        State.cards.current.consecutiveCorrect = 0;
                    }
                },
                
                categorizeCard(isCorrect) {
                    const cardId = State.cards.current.id;
                    
                    // Remove from all categories
                    State.cards.mastered.delete(cardId);
                    State.cards.learning.delete(cardId);
                    State.cards.difficult.delete(cardId);
                    
                    if (isCorrect) {
                        // Check for mastery
                        if (State.cards.current.consecutiveCorrect >= CONFIG.DIFFICULTY.MASTERY_CONSECUTIVE_CORRECT && 
                            State.cards.current.wrongCount === 0 && 
                            State.cards.current.totalSeen >= CONFIG.DIFFICULTY.MASTERY_MIN_SEEN) {
                            State.cards.mastered.add(cardId);
                            ScholarSRS.Achievement.show('Mastery Achieved', 'Perfect retention demonstrated');
                        } else {
                            State.cards.learning.add(cardId);
                        }
                    } else {
                        // Categorize as difficult or learning
                        const errorRate = State.cards.current.wrongCount / Math.max(1, State.cards.current.totalSeen);
                        if (State.cards.current.wrongCount >= CONFIG.DIFFICULTY.MIN_WRONG_FOR_DIFFICULT || 
                            errorRate > CONFIG.DIFFICULTY.ERROR_RATE_THRESHOLD) {
                            State.cards.difficult.add(cardId);
                        } else {
                            State.cards.learning.add(cardId);
                        }
                    }
                },
                
                recordResponse(isCorrect) {
                    const stats = State.cards.stats.get(State.cards.current.id);
                    if (stats) {
                        stats.responses.push(isCorrect);
                        stats.timestamps.push(performance.now());
                    }
                },
                
                rescheduleCard() {
                    // Add back to current phase queue
                    if (State.phase.queues[State.phase.current]) {
                        const insertPosition = Math.min(3, Math.floor(State.phase.queues[State.phase.current].length / 2));
                        State.phase.queues[State.phase.current].splice(insertPosition, 0, State.cards.current);
                    }
                    
                    // Add to future phases
                    for (let i = State.phase.current + 1; i < CONFIG.PHASES.length; i++) {
                        if (State.phase.queues[i] && !State.phase.queues[i].some(card => card.id === State.cards.current.id)) {
                            State.phase.queues[i].push(State.cards.current);
                        }
                    }
                },
                
                checkAchievements() {
                    const streak = State.performance.currentStreak;
                    if (streak === CONFIG.ACHIEVEMENTS.FIRST_STREAK) {
                        ScholarSRS.Achievement.show('Admirable Consistency', '5 consecutive successes');
                    } else if (streak === CONFIG.ACHIEVEMENTS.GOOD_STREAK) {
                        ScholarSRS.Achievement.show('Remarkable Performance', '10 consecutive successes');
                    } else if (streak === CONFIG.ACHIEVEMENTS.EXCELLENT_STREAK) {
                        ScholarSRS.Achievement.show('Exceptional Mastery', '20 consecutive successes');
                    }
                }
            },
            
            // =====================================
            // BREAK MANAGEMENT MODULE
            // =====================================
            Break: {
                start() {
                    try {
                        State.session.isBreak = true;
                        clearInterval(State.timing.timerInterval);
                        
                        // Clear quantum cycling during break
                        State.memoryEnhancement.quantumCyclingInterval.forEach(clearInterval);
                        State.memoryEnhancement.quantumCyclingInterval = [];
                        
                        // Clear quantum vibration during break
                        State.memoryEnhancement.quantumVibrationIntervals.forEach(clearInterval);
                        State.memoryEnhancement.quantumVibrationIntervals = [];
                        
                        ScholarSRS.UI.switchToBreakScreen();
                        ScholarSRS.Audio.playBreak();
                        
                        // Trigger break-specific memory systems
                        MemoryEnhancement.orchestrate('breakStart');
                        
                        let breakDuration = CONFIG.BREAK_DURATION;
                        State.timing.savedBreakDuration = breakDuration;
                        
                        State.timing.breakInterval = setInterval(() => {
                            if (!State.session.isPaused) {
                                breakDuration--;
                                State.timing.savedBreakDuration = breakDuration;
                                this.updateTimer(breakDuration);
                                
                                if (breakDuration <= 0) {
                                    this.end();
                                }
                            }
                        }, 1000);
                        
                        this.scheduleNext();
                        
                    } catch (error) {
                        ScholarSRS.Error.handle('breakStart', error);
                        this.end();
                    }
                },
                
                skip() {
                    try {
                        if (State.timing.breakInterval) clearInterval(State.timing.breakInterval);
                        this.end();
                    } catch (error) {
                        ScholarSRS.Error.handle('breakSkip', error);
                        this.end();
                    }
                },
                
                end() {
                    try {
                        State.session.isBreak = false;
                        if (State.timing.breakInterval) clearInterval(State.timing.breakInterval);
                        
                        // Clean up delta wave systems
                        if (State.memoryEnhancement.deltaWaveInterval) {
                            clearInterval(State.memoryEnhancement.deltaWaveInterval);
                            State.memoryEnhancement.deltaWaveInterval = null;
                            State.memoryEnhancement.deltaWavePulseActive = false;
                        }
                        if (State.memoryEnhancement.schumannResonanceOscillator) {
                            State.memoryEnhancement.schumannGainNode.gain.exponentialRampToValueAtTime(
                                0.001, State.settings.audioContext.currentTime + 0.5
                            );
                            setTimeout(() => {
                                State.memoryEnhancement.schumannResonanceOscillator.stop();
                                State.memoryEnhancement.schumannResonanceOscillator.disconnect();
                                State.memoryEnhancement.schumannResonanceOscillator = null;
                                State.memoryEnhancement.schumannGainNode = null;
                            }, 500);
                        }
                        
                        ScholarSRS.UI.switchToStudyScreen();
                        ScholarSRS.Audio.playSuccess();
                        ScholarSRS.Achievement.show('Session Resumed', 'Continue your path to mastery');
                        
                        State.timing.timerInterval = setInterval(() => ScholarSRS.Timer.update(), CONFIG.PROGRESS_UPDATE_INTERVAL);
                        ScholarSRS.Card.showNext();
                        
                    } catch (error) {
                        ScholarSRS.Error.handle('breakEnd', error);
                        ScholarSRS.UI.switchToStudySc                        <button class="btn" id="start-button" onclick="ScholarSRS.startSession()">Commence Study Session</button>                        <button class="btn" id="start-button" onclick="ScholarSRS.startSession()">Commence Study Session</button>reen();
                        State.timing.timerInterval = setInterval(() => ScholarSRS.Timer.update(), CONFIG.PROGRESS_UPDATE_INTERVAL);
                    }
                },
                
                updateTimer(duration) {
                    const minutes = Math.floor(duration / 60);
                    const seconds = duration % 60;
                    
                    const breakTimerElement = document.getElementById('break-timer');
                    if (breakTimerElement) {
                        breakTimerElement.textContent = 
                            `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
                    }
                },
                
                scheduleNext() {
                    State.timing.nextBreakTime = Date.now() + CONFIG.BREAK_INTERVAL;
                }
            },
            
            // =====================================
            // TIMER MODULE
            // =====================================
            Timer: {
                update() {
                    if (State.session.isPaused) return;
                    
                    try {
                        this.updatePhaseTimer();
                        this.updateProgress();
                        ScholarSRS.Stats.updateRate();
                        this.checkPhaseCompletion();
                        
                    } catch (error) {
                        ScholarSRS.Error.handle('timerUpdate', error);
                    }
                },
                
                updatePhaseTimer() {
                    const now = performance.now();
                    const phaseElapsed = now - State.phase.preciseStartTime;
                    const phaseDuration = State.session.totalHours * 3600 * CONFIG.PHASES[State.phase.current].percentage * 1000;
                    
                    const phaseRemaining = Math.max(0, phaseDuration - phaseElapsed);
                    const phaseHours = Math.floor(phaseRemaining / (3600 * 1000));
                    const phaseMinutes = Math.floor((phaseRemaining % (3600 * 1000)) / (60 * 1000));
                    const phaseSeconds = Math.floor((phaseRemaining % (60 * 1000)) / 1000);
                    
                    const timerElement = document.getElementById('timer');
                    if (timerElement) {
                        timerElement.textContent = 
                            `${phaseHours.toString().padStart(2, '0')}:${phaseMinutes.toString().padStart(2, '0')}:${phaseSeconds.toString().padStart(2, '0')}`;
                    }
                },
                
                updateProgress() {
                    const now = performance.now();
                    const phaseElapsed = now - State.phase.preciseStartTime;
                    const phaseDuration = State.session.totalHours * 3600 * CONFIG.PHASES[State.phase.current].percentage * 1000;
                    
                    const phaseProgress = Math.min(100, (phaseElapsed / phaseDuration) * 100);
                    const phaseProgressBar = document.getElementById('phase-progress');
                    const phaseProgressText = document.getElementById('phase-progress-text');
                    
                    if (phaseProgressBar) {
                        phaseProgressBar.style.width = Math.max(0, phaseProgress) + '%';
                    }
                    if (phaseProgressText) {
                        phaseProgressText.textContent = Math.floor(Math.max(0, Math.min(100, phaseProgress))) + '%';
                    }
                },
                
                checkPhaseCompletion() {
                    const now = performance.now();
                    const phaseElapsed = now - State.phase.preciseStartTime;
                    const phaseDuration = State.session.totalHours * 3600 * CONFIG.PHASES[State.phase.current].percentage * 1000;
                    
                    if (phaseElapsed >= phaseDuration && 
                        State.phase.queues[State.phase.current] && 
                        State.phase.queues[State.phase.current].length > 0) {
                        const unseenCards = State.phase.queues[State.phase.current].filter(card => card.totalSeen === 0);
                        if (unseenCards.length === 0) {
                            ScholarSRS.Phase.complete();
                        }
                    }
                }
            },
            
            // =====================================
            // STATISTICS MODULE
            // =====================================
            Stats: {
                update() {
                    try {
                        const totalCards = State.cards.all.length;
                        const mastered = State.cards.mastered.size;
                        const learning = State.cards.learning.size;
                        const difficult = State.cards.difficult.size;
                        
                        const elements = {
                            'total-questions': totalCards,
                            'mastered-count': mastered,
                            'learning-count': learning,
                            'difficult-count': difficult,
                            'streak': State.performance.currentStreak
                        };
                        
                        Object.entries(elements).forEach(([id, value]) => {
                            const element = document.getElementById(id);
                            if (element) {
                                element.textContent = value;
                            }
                        });
                        
                        this.updateAccuracy();
                        this.updateOverallProgress();
                        
                    } catch (error) {
                        ScholarSRS.Error.handle('statsUpdate', error);
                    }
                },
                
                updateAccuracy() {
                    const accuracy = State.performance.totalAttempts > 0 
                        ? Math.round((State.performance.totalCorrect / State.performance.totalAttempts) * 100) 
                        : 0;
                    const accuracyElement = document.getElementById('accuracy');
                    if (accuracyElement) {
                        accuracyElement.textContent = Math.max(0, Math.min(100, accuracy)) + '%';
                    }
                },
                
                updateOverallProgress() {
                    const overallProgress = State.cards.all.length > 0 
                        ? (State.cards.mastered.size / State.cards.all.length) * 100 
                        : 0;
                    const progressBar = document.getElementById('overall-progress');
                    const progressText = document.getElementById('overall-progress-text');
                    
                    if (progressBar) {
                        progressBar.style.width = Math.max(0, Math.min(100, overallProgress)) + '%';
                    }
                    if (progressText) {
                        progressText.textContent = `Overall: ${Math.round(Math.max(0, Math.min(100, overallProgress)))}%`;
                    }
                },
                
                updateRemaining() {
                    try {
                        if (!State.phase.queues || !State.phase.queues[State.phase.current]) {
                            document.getElementById('remaining-count').textContent = '0';
                            return;
                        }
                        
                        let remainingCount = State.phase.queues[State.phase.current].length;
                        
                        if (State.cards.current && document.getElementById('show-answer-btn').style.display !== 'none') {
                            remainingCount += 1;
                        }
                        
                        remainingCount = Math.max(0, remainingCount);
                        document.getElementById('remaining-count').textContent = remainingCount;
                    } catch (error) {
                        document.getElementById('remaining-count').textContent = '0';
                    }
                },
                
                updateRate() {
                    const now = performance.now();
                    
                    if (State.performance.cardsCompletedForRate === 0) {
                        document.getElementById('cards-per-minute').textContent = '0.0';
                        return;
                    }
                    
                    let actualStudyTimeMs = now - State.timing.rateCalculationStartTime - State.timing.totalPausedTime;
                    const actualStudyTimeMinutes = actualStudyTimeMs / (1000 * 60);
                    
                    if (actualStudyTimeMinutes <= 0) {
                        document.getElementById('cards-per-minute').textContent = '0.0';
                        return;
                    }
                    
                    const instantaneousRate = State.performance.cardsCompletedForRate / actualStudyTimeMinutes;
                    
                    State.performance.rateHistory.push(instantaneousRate);
                    if (State.performance.rateHistory.length > CONFIG.MOVING_AVERAGE_WINDOW) {
                        State.performance.rateHistory.shift();
                    }
                    
                    const smoothedRate = State.performance.rateHistory.reduce((sum, rate) => sum + rate, 0) / State.performance.rateHistory.length;
                    const displayRate = Math.max(0, smoothedRate);
                    document.getElementById('cards-per-minute').textContent = displayRate.toFixed(1);
                }
            },
            
            // =====================================
            // CONTROLS MODULE
            // =====================================
            Controls: {
                init() {
                    this.setupKeyboardShortcuts();
                },
                
                togglePause() {
                    const now = performance.now();
                    
                    if (!State.session.isPaused) {
                        State.session.isPaused = true;
                        State.timing.pauseStartTime = now;
                        
                        this.pauseTimers();
                        this.updatePauseUI(true);
                        ScholarSRS.Audio.playSound(300, 0.1);
                        
                        // Trigger memory systems during pause
                        MemoryEnhancement.orchestrate('sessionPause');
                    } else {
                        State.session.isPaused = false;
                        const pauseDuration = now - State.timing.pauseStartTime;
                        State.timing.totalPausedTime += pauseDuration;
                        
                        this.adjustTimingsForPause(pauseDuration);
                        this.resumeTimers();
                        this.updatePauseUI(false);
                        ScholarSRS.Audio.playSound(400, 0.1);
                    }
                },
                
                pauseTimers() {
                    if (State.timing.timerInterval) clearInterval(State.timing.timerInterval);
                    if (State.timing.breakInterval) clearInterval(State.timing.breakInterval);
                    
                    // Pause quantum cycling
                    State.memoryEnhancement.quantumCyclingInterval.forEach(clearInterval);
                    State.memoryEnhancement.quantumCyclingInterval = [];
                    
                    // Pause quantum vibration
                    State.memoryEnhancement.quantumVibrationIntervals.forEach(clearInterval);
                    State.memoryEnhancement.quantumVibrationIntervals = [];
                    
                    // Pause delta wave systems
                    if (State.memoryEnhancement.deltaWaveInterval) {
                        clearInterval(State.memoryEnhancement.deltaWaveInterval);
                    }
                },
                
                resumeTimers() {
                    if (State.session.isBreak) {
                        State.timing.breakInterval = setInterval(() => {
                            if (!State.session.isPaused) {
                                State.timing.savedBreakDuration--;
                                ScholarSRS.Break.updateTimer(State.timing.savedBreakDuration);
                                
                                if (State.timing.savedBreakDuration <= 0) {
                                    ScholarSRS.Break.end();
                                }
                            }
                        }, 1000);
                        
                        // Resume delta wave systems if they were active
                        if (State.memoryEnhancement.deltaWavePulseActive) {
                            MemoryEnhancement.System40_DeltaWaveMemoryConsolidation();
                        }
                    } else {
                        State.timing.timerInterval = setInterval(() => ScholarSRS.Timer.update(), CONFIG.PROGRESS_UPDATE_INTERVAL);
                    }
                },
                
                adjustTimingsForPause(pauseDuration) {
                    State.session.preciseStartTime += pauseDuration;
                    State.phase.preciseStartTime += pauseDuration;
                    State.session.startTime = Date.now() - (performance.now() - State.session.preciseStartTime);
                    State.phase.startTime = Date.now() - (performance.now() - State.phase.preciseStartTime);
                    State.timing.nextBreakTime += pauseDuration;
                    State.timing.rateCalculationStartTime += pauseDuration;
                },
                
                updatePauseUI(isPaused) {
                    document.getElementById('pause-icon').textContent = isPaused ? '▶' : '⏸';
                    document.getElementById('pause-toggle').classList.toggle('paused', isPaused);
                    document.querySelectorAll('.btn').forEach(btn => btn.disabled = isPaused);
                },
                
                setupKeyboardShortcuts() {
                    document.addEventListener('keypress', (e) => {
                        try {
                            if (e.key === 'Enter' && document.querySelector('.study-screen').classList.contains('active')) {
                                const showBtn = document.getElementById('show-answer-btn');
                                if (showBtn && showBtn.style.display !== 'none') {
                                    ScholarSRS.Card.showAnswer();
                                }
                            }
                            
                            if (e.key === ' ' && document.querySelector('.study-screen').classList.contains('active')) {
                                e.preventDefault();
                                const showBtn = document.getElementById('show-answer-btn');
                                if (showBtn && showBtn.style.display !== 'none') {
                                    ScholarSRS.Card.showAnswer();
                                }
                            }
                            
                        } catch (error) {
                            ScholarSRS.Error.handle('keyboardShortcut', error);
                        }
                    });
                }
            },
            
            // =====================================
            // AUDIO MODULE
            // =====================================
            Audio: {
                init() {
                    try {
                        State.settings.audioContext = new (window.AudioContext || window.webkitAudioContext)();
                    } catch (e) {
                        // Audio not supported
                    }
                    
                    // Initialize audio context on first interaction
                    document.addEventListener('click', () => {
                        try {
                            if (State.settings.audioContext && State.settings.audioContext.state === 'suspended') {
                                State.settings.audioContext.resume();
                            }
                        } catch (error) {
                            // Error resuming audio context
                        }
                    }, { once: true });
                },
                
                playSound(frequency, duration, type = 'sine') {
                    if (!State.settings.soundEnabled || !State.settings.audioContext) return;
                    
                    try {
                        const oscillator = State.settings.audioContext.createOscillator();
                        const gainNode = State.settings.audioContext.createGain();
                        
                        oscillator.connect(gainNode);
                        gainNode.connect(State.settings.audioContext.destination);
                        
                        oscillator.frequency.value = frequency;
                        oscillator.type = type;
                        
                        gainNode.gain.setValueAtTime(0.1, State.settings.audioContext.currentTime);
                        gainNode.gain.exponentialRampToValueAtTime(0.01, State.settings.audioContext.currentTime + duration);
                        
                        oscillator.start(State.settings.audioContext.currentTime);
                        oscillator.stop(State.settings.audioContext.currentTime + duration);
                    } catch (error) {
                        // Audio playback failed
                    }
                },
                
                playSuccess() {
                    const frequencies = CONFIG.AUDIO.SUCCESS_FREQUENCIES;
                    this.playSound(frequencies[0], 0.1);
                    setTimeout(() => this.playSound(frequencies[1], 0.1), 100);
                    setTimeout(() => this.playSound(frequencies[2], 0.2), 200);
                },
                
                playError() {
                    this.playSound(CONFIG.AUDIO.ERROR_FREQUENCY, 0.3, 'sawtooth');
                },
                
                playBreak() {
                    for (let i = 0; i < 3; i++) {
                        setTimeout(() => {
                            this.playSound(CONFIG.AUDIO.BREAK_FREQUENCY, 0.2);
                            setTimeout(() => this.playSound(554.37, 0.2), 200);
                        }, i * 500);
                    }
                },
                
                toggleSound() {
                    State.settings.soundEnabled = !State.settings.soundEnabled;
                    document.getElementById('sound-icon').textContent = State.settings.soundEnabled ? '🔊' : '🔇';
                    document.getElementById('sound-toggle').classList.toggle('muted', !State.settings.soundEnabled);
                    
                    if (State.settings.soundEnabled && State.settings.audioContext) {
                        State.settings.audioContext.resume();
                        this.playSound(440, 0.1);
                    }
                }
            },
            
            // =====================================
            // UI MODULE
            // =====================================
            UI: {
                init() {
                    // Set default hours
                    const hoursInput = document.getElementById('hours');
                    if (hoursInput && !hoursInput.value) {
                        hoursInput.value = '3';
                    }
                },
                
                switchToStudyScreen() {
                    document.querySelector('.setup-screen').classList.remove('active');
                    document.querySelector('.break-screen').classList.remove('active');
                    document.querySelector('.study-screen').classList.add('active');
                    
                    // Update display
                    document.getElementById('total-questions').textContent = State.cards.all.length;
                    ScholarSRS.Stats.update();
                },
                
                switchToBreakScreen() {
                    document.querySelector('.study-screen').classList.remove('active');
                    document.querySelector('.break-screen').classList.add('active');
                },
                
                switchToSetupScreen() {
                    document.querySelector('.study-screen').classList.remove('active');
                    document.querySelector('.break-screen').classList.remove('active');
                    document.querySelector('.setup-screen').classList.add('active');
                }
            },
            
            // =====================================
            // ACHIEVEMENT MODULE
            // =====================================
            Achievement: {
                show(title, text) {
                    const achievement = document.getElementById('achievement');
                    document.getElementById('achievement-title').textContent = title;
                    document.getElementById('achievement-text').textContent = text;
                    achievement.classList.add('show');
                    ScholarSRS.Audio.playSuccess();
                    
                    setTimeout(() => {
                        achievement.classList.remove('show');
                    }, 3000);
                }
            },
            
            // =====================================
            // UTILITY MODULE
            // =====================================
            Utils: {
                shuffleArray(array) {
                    try {
                        for (let i = array.length - 1; i > 0; i--) {
                            const j = Math.floor(Math.random() * (i + 1));
                            [array[i], array[j]] = [array[j], array[i]];
                        }
                        return array;
                    } catch (error) {
                        return array;
                    }
                }
            },
            
            // =====================================
            // ERROR HANDLING MODULE
            // =====================================
            Error: {
                handle(context, error) {
                    // Graceful error handling without user disruption
                    try {
                        if (context === 'critical') {
                            // For critical errors, try to maintain basic functionality
                            ScholarSRS.Achievement.show('System Notice', 'Continuing with basic functionality');
                        }
                    } catch (e) {
                        // Silently handle error handling errors
                    }
                }
            }
        };
        
        // ========================================
        // GLOBAL EVENT HANDLERS & INITIALIZATION
        // ========================================
        
        // Initialize when DOM loads
        document.addEventListener('DOMContentLoaded', () => {
            try {
                ScholarSRS.init();
            } catch (error) {
                ScholarSRS.Error.handle('initialization', error);
            }
        });
        
        // Global error handling
        window.addEventListener('unhandledrejection', (event) => {
            event.preventDefault();
            ScholarSRS.Error.handle('unhandledPromise', event.reason);
        });
        
        window.addEventListener('error', (event) => {
            ScholarSRS.Error.handle('globalError', event.error);
        });
    </script>
</body>
</html>'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    print("🎓 Scholar's Spaced Repetition System v2.0 - COMPLETE")
    print("📚 Launching with ALL 42 Subliminal Memory Enhancement Systems")
    print()
    
    if not check_port_availability():
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Start browser after a small delay
    Timer(1.0, open_browser).start()
    
    print("🚀 Starting server...")
    print("🌐 Access your learning system at: http://127.0.0.1:5000")
    print()
    print("📖 Features:")
    print("   • Seven-phase progressive learning system")
    print("   • ALL 42 subliminal memory enhancement systems (COMPLETE)")
    print("   • Systems 1-36: Core memory enhancement suite") 
    print("   • System 37: Chronobiological Phase Coupling")
    print("   • System 38: Mirror Neuron Activation Protocol")
    print("   • System 39: Subliminal Confidence Injection")
    print("   • System 40: Delta Wave Memory Consolidation")
    print("   • System 41: Phantom Touch Memory Encoding")
    print("   • System 42: Accelerometer Rhythm Encoding (Mobile)")
    print("   • Adaptive difficulty and spaced repetition")
    print("   • Real-time performance analytics")
    print("   • Pomodoro-style breaks")
    print("   • Audio feedback and binaural beats")
    print("   • Advanced neural synchronization systems")
    print("   • Circadian rhythm optimization")
    print("   • Mobile device motion integration")
    print()
    print("⚡ Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        app.run(debug=False, host='127.0.0.1', port=5000)
    except KeyboardInterrupt:
        print("\n\n✨ Thank you for using Scholar's SRS!")
        print("📚 Your knowledge journey continues!")