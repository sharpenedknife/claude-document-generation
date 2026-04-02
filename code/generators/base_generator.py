"""
Docgen Generator Framework
All generators inherit from this base class
"""

import json
from datetime import datetime
from typing import Dict, List, Any
import anthropic

# Load prompt templates
def load_prompt(prompt_name: str) -> str:
    """Load optimized prompt from file"""
    try:
        with open(f'code/prompts/{prompt_name}_prompt.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt not found: {prompt_name}_prompt.txt")

# DOC_CANONICAL_TEMPLATE
DOC_CANONICAL_TEMPLATE = """---
title: {title}
description: {description}
version: {version}
date: {date}
author: Docgen
category: {category}
status: {status}
tags: {tags}
---

{content}
"""

class BaseGenerator:
    """Base class for all generators"""
    
    def __init__(self, project_type: str, prompt_name: str):
        self.project_type = project_type
        self.prompt_name = prompt_name
        self.prompt = load_prompt(prompt_name)
        self.client = anthropic.Anthropic()
    
    def format_answers(self, answers: Dict[str, str]) -> str:
        """Format questionnaire answers into prompt context"""
        formatted = "User has provided the following information:\n\n"
        for i, (key, value) in enumerate(answers.items(), 1):
            formatted += f"Q{i}: {value}\n"
        return formatted
    
    def generate_content(self, answers: Dict[str, str]) -> str:
        """Call Claude API to generate document content"""
        user_prompt = self.format_answers(answers)
        
        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=3000,
            system=self.prompt,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )
        
        return response.content[0].text
    
    def populate_template(self, content: str, metadata: Dict[str, str]) -> str:
        """Fill DOC_CANONICAL_TEMPLATE with generated content"""
        today = datetime.now().strftime("%Y-%m-%d")
        
        doc = DOC_CANONICAL_TEMPLATE.format(
            title=metadata.get("title", "Document"),
            description=metadata.get("description", ""),
            version=metadata.get("version", "1.0"),
            date=metadata.get("date", today),
            category=metadata.get("category", "General"),
            status=metadata.get("status", "DRAFT"),
            tags=json.dumps(metadata.get("tags", [])),
            content=content
        )
        
        return doc
    
    def generate(self, answers: Dict[str, str]) -> Dict[str, Any]:
        """Generate complete document"""
        # Generate content
        content = self.generate_content(answers)
        
        # Populate template
        metadata = {
            "title": self.get_title(),
            "description": self.get_description(),
            "version": "1.0",
            "category": self.get_category(),
            "status": "PRODUCTION_READY",
            "tags": self.get_tags()
        }
        
        doc = self.populate_template(content, metadata)
        
        return {
            "filename": self.get_filename(),
            "content": doc,
            "metadata": {
                **metadata,
                "word_count": len(content.split()),
                "token_estimate": int(len(content) / 4)  # rough estimate
            }
        }
    
    def get_title(self) -> str:
        raise NotImplementedError
    
    def get_description(self) -> str:
        raise NotImplementedError
    
    def get_category(self) -> str:
        raise NotImplementedError
    
    def get_filename(self) -> str:
        raise NotImplementedError
    
    def get_tags(self) -> List[str]:
        raise NotImplementedError


# Specific generators
class PRDGenerator(BaseGenerator):
    def __init__(self):
        super().__init__("prd", "prd")
    
    def get_title(self) -> str:
        return "Product Requirements Document"
    
    def get_description(self) -> str:
        return "Product requirements, features, success metrics, and acceptance criteria"
    
    def get_category(self) -> str:
        return "Product"
    
    def get_filename(self) -> str:
        return "PRD.md"
    
    def get_tags(self) -> List[str]:
        return ["prd", "requirements", "product", "acceptance-criteria"]


class UXGenerator(BaseGenerator):
    def __init__(self):
        super().__init__("ux", "ux")
    
    def get_title(self) -> str:
        return "UX Requirements"
    
    def get_description(self) -> str:
        return "User flows, wireframe descriptions, interaction specifications"
    
    def get_category(self) -> str:
        return "Design"
    
    def get_filename(self) -> str:
        return "UX_Requirements.md"
    
    def get_tags(self) -> List[str]:
        return ["ux", "design", "wireframes", "interactions"]


class SpecifiersGenerator(BaseGenerator):
    def __init__(self):
        super().__init__("specifiers", "specifiers")
    
    def get_title(self) -> str:
        return "Technical Specifications"
    
    def get_description(self) -> str:
        return "Tech stack, data model, API endpoints, security, deployment"
    
    def get_category(self) -> str:
        return "Engineering"
    
    def get_filename(self) -> str:
        return "specifiers.md"
    
    def get_tags(self) -> List[str]:
        return ["specs", "technical", "architecture", "api"]


class MonetizationGenerator(BaseGenerator):
    def __init__(self):
        super().__init__("monetization", "monetization")
    
    def get_title(self) -> str:
        return "Monetization Strategy"
    
    def get_description(self) -> str:
        return "Pricing model, tiers, revenue projections, packaging"
    
    def get_category(self) -> str:
        return "Business"
    
    def get_filename(self) -> str:
        return "Monetization.md"
    
    def get_tags(self) -> List[str]:
        return ["monetization", "pricing", "revenue", "business"]


class DevPlanGenerator(BaseGenerator):
    def __init__(self):
        super().__init__("dev_plan", "dev_plan")
    
    def get_title(self) -> str:
        return "Development Plan"
    
    def get_description(self) -> str:
        return "Sprint breakdown, task list, timeline, dependencies, milestones"
    
    def get_category(self) -> str:
        return "Engineering"
    
    def get_filename(self) -> str:
        return "Development_Plan.md"
    
    def get_tags(self) -> List[str]:
        return ["dev-plan", "roadmap", "sprints", "timeline"]


class CustomGenerator(BaseGenerator):
    def __init__(self):
        super().__init__("custom", "custom")
    
    def get_title(self) -> str:
        return "Custom Documentation"
    
    def get_description(self) -> str:
        return "User-defined custom documentation"
    
    def get_category(self) -> str:
        return "Custom"
    
    def get_filename(self) -> str:
        return "Custom_Document.md"
    
    def get_tags(self) -> List[str]:
        return ["custom", "user-defined"]


class SkillGenerator(BaseGenerator):
    def __init__(self):
        super().__init__("skill", "skill")
    
    def get_title(self) -> str:
        return "AI Skill Definition"
    
    def get_description(self) -> str:
        return "Reusable AI skill with triggers, capabilities, and examples"
    
    def get_category(self) -> str:
        return "Skill"
    
    def get_filename(self) -> str:
        return "Skill_Definition.md"
    
    def get_tags(self) -> List[str]:
        return ["skill", "reusable", "ai-tool"]


class ProjectGenerator(BaseGenerator):
    def __init__(self):
        super().__init__("project", "project")
    
    def get_title(self) -> str:
        return "Claude Project Instructions"
    
    def get_description(self) -> str:
        return "System message, role, capabilities, workflows for Claude Project"
    
    def get_category(self) -> str:
        return "Project"
    
    def get_filename(self) -> str:
        return "PROJECT_INSTRUCTIONS.md"
    
    def get_tags(self) -> List[str]:
        return ["project", "claude-projects", "instructions"]


class SummaryGenerator(BaseGenerator):
    def __init__(self):
        super().__init__("summary", "summary")
    
    def get_title(self) -> str:
        return "Executive Summary"
    
    def get_description(self) -> str:
        return "High-level synthesis of documents and key insights"
    
    def get_category(self) -> str:
        return "Analysis"
    
    def get_filename(self) -> str:
        return "Executive_Summary.md"
    
    def get_tags(self) -> List[str]:
        return ["summary", "synthesis", "executive"]


# Factory function
def get_generator(project_type: int) -> BaseGenerator:
    """Get the appropriate generator for a project type"""
    generators = {
        1: PRDGenerator,
        2: PRDGenerator,  # Feature Release also uses PRD
        3: DevPlanGenerator,  # Workflow Automation
        4: MonetizationGenerator,  # Revenue Stream
        5: CustomGenerator,  # Brand Marketing (for now)
        6: CustomGenerator,  # Product Marketing (for now)
        7: SummaryGenerator,  # Summarize Files
        8: CustomGenerator,  # Custom Documentation
        9: SkillGenerator,  # AI Skill
        10: ProjectGenerator  # Claude Project
    }
    
    generator_class = generators.get(project_type, CustomGenerator)
    return generator_class()
