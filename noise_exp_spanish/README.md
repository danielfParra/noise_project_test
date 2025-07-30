# Noise Experiment (Spanish) - oTree Cognitive Assessment Study

## Overview
This is an oTree-based psychological experiment designed to assess cognitive 
performance (working memory) and sound sensitivity in Spanish-speaking 
participants. The study uses a counterbalanced design with randomized 
n-back task order and includes comprehensive demographic 
and misophonia assessments.

## System Requirements

### **Python Version**
- **Python 3.12.4** (Required)

### **oTree Framework**
- **oTree 5.11.1** (Core experimental platform)

## Dependencies

### Core Framework Components 
otree==5.11.1 
SQLAlchemy==1.3.22
WTForms==2.3.3
WTForms-SQLAlchemy==0.2

### File Handling & Utilities
aiofiles==0.6.0 
python-multipart==0.0.5 
click==7.1.2

### Security & Templating
MarkupSafe==1.1.1 
itsdangerous==1.1.1

### Compatibility
six==1.16.0

## Installation

1. **Ensure Python 3.12.4 is installed**
2. **Clone or download this project**
3. **Navigate to the project directory**
4. **Install dependencies:**
   ```bash
   pip install -r requirements_freeze.txt
   
## Full Experimental Sessions (Counterbalanced)

order_2M3: Order A - 2-Back → Memory → 3-Back
order_3M2: Order B - 3-Back → Memory → 2-Back

### Session Flow (7 Components Each)

Consent - Informed consent form
Welcome - Instructions and setup
First N-Back - Either 2-Back or 3-Back (randomized)
Memory Task - Word-based memory assessment (fixed position)
Second N-Back - Complementary task (counterbalanced)
Payment Info - Compensation details
Survey - Demographics and Misophonia Assessment Scale

## Development Notes

Developed with oTree 5.11.1 framework
Compatible with Python 3.12.4
All text content presented in Spanish
Counterbalancing achieved through separate session configurations

## Support

For technical issues or questions about the experimental design, refer to the oTree documentation or contact the research team.