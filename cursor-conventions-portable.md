# 📚 Cursor AI Dual-Version Content Conventions

**Portable guidelines for creating educational content in any project.**

---

## Core Principle: Always Create Two Versions

When creating any educational content (guides, documentation, examples), **ALWAYS** create TWO versions:

### **Simple Version (-simple suffix)**
**Purpose**: Quick reference, beginner-friendly, essential concepts only

### **Cursor Version (-cursor suffix)**  
**Purpose**: Comprehensive, detailed, use your full discerning judgment

---

## Simple Version Requirements

**CRITICAL**: Simple versions must follow these EXACT guidelines:

### **Markdown Style:**
```markdown
# Topic Name

**1. Core Concept:**
Brief, direct explanation of what it does.

**2. Basic Usage:**
When and why to use it.

```language
# Essential example only
simple_code = "demonstration"
print(simple_code)
```

**3. Key Points:**
- Bullet points for important facts
- Keep explanations under 2 sentences
- Focus on "what" not "why" or "how"
```

### **Code Style:**
```python
# Simple version - basic demonstration
variable = "value"
result = function(variable)
print(result)
```

### **Simple Version Rules:**
✅ **DO:**
- Use clean numbered sections (`**1. Topic:**`)
- Keep explanations to 1-2 sentences maximum
- Include only ONE essential example per concept
- Use basic bullet points for lists
- Focus on core functionality only
- Use minimal, clean formatting

❌ **DON'T:**
- Add context, background, or "why" explanations
- Include multiple examples or variations
- Use complex formatting or styling
- Add performance notes or alternatives
- Include real-world scenarios
- Add comparisons or detailed explanations

---

## Cursor Version Freedom

**Cursor Version = Your Full Discerning Judgment**

For cursor versions, use your complete expertise and judgment to create:
- Comprehensive explanations with full context
- Multiple real-world examples and use cases
- Performance considerations and best practices
- Alternative approaches and comparisons
- Advanced patterns and edge cases
- Rich formatting and detailed organization
- Industry-specific scenarios when relevant
- "Without this concept" comparisons when valuable
- Inline outputs, debugging tips, and practical notes

**No restrictions** - make cursor versions as detailed and valuable as you deem appropriate for the topic and audience.

---

## File Naming Convention

```
topic-name-simple.md          # Minimal reference version
topic-name-cursor.md          # Your comprehensive version
example-simple.py             # Basic demonstration
example-cursor.py             # Advanced scenarios
```

---

## Quality Standards

### **Simple Version Tests:**
- Can be understood in under 3 minutes
- Contains only essential information
- Could serve as a quick cheat sheet
- No scrolling needed for basic concepts

### **Cursor Version Tests:**
- Provides deep understanding of the topic
- Includes practical applications
- Shows your full expertise and knowledge
- Serves as comprehensive learning resource

---

## Workflow

1. **Create Simple Version First**
   - Follow the strict simple guidelines above
   - Focus only on essential concepts
   - Keep it minimal and clean

2. **Create Cursor Version Second**
   - Use your full judgment and expertise
   - Add all context, examples, and depth you think valuable
   - No restrictions on complexity or length

---

## Benefits

🎯 **Universal Application**: Works for any topic or project  
🎯 **Learner Choice**: Quick reference vs deep learning  
🎯 **Teaching Flexibility**: Appropriate depth for different needs  
🎯 **Cursor Autonomy**: Full freedom for comprehensive versions  
🎯 **Consistent Simple Style**: Predictable quick-reference format  

---

## Simple Version Template

Copy this template for any simple version:

```markdown
# [Topic Name]

**1. What it is:**
One sentence definition.

**2. Basic usage:**
When to use it.

```[language]
# Single essential example
basic_code = "demonstration"
```

**3. Key points:**
- Essential fact 1
- Essential fact 2
- Essential fact 3
```

---

## Implementation Notes

- **Simple = Strict rules** (follow guidelines exactly)
- **Cursor = Your judgment** (use full expertise)
- **Always create both** for any educational content
- **Simple first** to ensure core concepts are clear
- **Test readability** on someone unfamiliar with the topic

This approach ensures consistent, scannable reference materials alongside comprehensive learning resources tailored to your expertise. 