# Chat-Based UI Wireframes

## Overview
The conversational UI allows users to request character builds through natural language input, with AI-generated responses displaying skills, items, and playstyle tips.

## Layout Structure

### Main Chat Interface
```
┌─────────────────────────────────────┐
│ Header: BuildCraft AI               │
├─────────────────────────────────────┤
│                                     │
│ Chat Messages Area                  │
│ - User messages (right-aligned)     │
│ - AI responses (left-aligned)       │
│ - Build suggestions with cards      │
│                                     │
├─────────────────────────────────────┤
│ Input Area:                         │
│ ┌─────────────────────────────────┐ │
│ │ Type your build request...      │ │
│ └─────────────────────────────────┘ │
│ [Send] [Clear]                      │
└─────────────────────────────────────┘
```

### Build Suggestion Card
```
┌─────────────────────────────────────┐
│ 🎮 Venom Paladin                    │
├─────────────────────────────────────┤
│ Skills: Blade, Alchemy, Restoration │
│ Key Item: Virulent Sword            │
│ Playstyle: Heal allies while        │
│           poisoning enemies         │
├─────────────────────────────────────┤
│ [Save Build] [Share] [Regenerate]   │
└─────────────────────────────────────┘
```

## Mobile Responsive Design
- Single column layout on mobile
- Full-width input area
- Collapsible build cards
- Touch-friendly buttons

## User Flow
1. User types build request (e.g., "stealthy alchemist")
2. AI processes request and generates build
3. Build displayed as interactive card
4. User can save, share, or regenerate build
5. Conversation history maintained

## Components Needed
- Chat container
- Message bubbles (user/AI)
- Input field with send button
- Build suggestion cards
- Action buttons (save, share, regenerate)
- Loading states
- Error handling 