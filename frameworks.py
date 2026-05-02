"""
Ethical Frameworks Knowledge Base
Extracted from COSC 643: Ethics of Artificial Intelligence (Maryville University)
Instructor: Palmer | Spring 2026

This module encodes the foundational, contemporary, and AI-specific ethical
frameworks taught throughout the course so that the agentic system can draw
on them during ethical reasoning.
"""

# ---------------------------------------------------------------------------
# 1. FOUNDATIONAL ETHICAL FRAMEWORKS
# ---------------------------------------------------------------------------

UTILITARIANISM = {
    "name": "Utilitarianism",
    "key_thinker": "Jeremy Bentham, John Stuart Mill",
    "core_idea": (
        "The consequences of our actions are the most important factor. "
        "We should strive to increase pleasure and minimize pain for the "
        "greatest number of people."
    ),
    "strengths": [
        "Provides a clear, quantifiable decision procedure",
        "Focuses on real-world outcomes rather than abstract duties",
        "Encourages consideration of the broadest possible impact",
    ],
    "weaknesses": [
        "Can justify harming individuals for the 'greater good'",
        "Predisposed to dehumanize individuals attached to data-driven systems",
        "Difficulty in measuring and comparing different types of pleasure/pain",
        "The Trolley Problem reveals tensions between passive and active harm",
    ],
    "tech_application": (
        "Tech is data-driven, so it trends toward utilitarian thinking. "
        "This means the field is predisposed to dehumanize individuals. "
        "We must be conscious of whether we are slipping into a purely "
        "mathematical understanding of how tech impacts us."
    ),
}

DEONTOLOGY = {
    "name": "Deontology (Kantian Ethics)",
    "key_thinker": "Immanuel Kant",
    "core_idea": (
        "The Categorical Imperative: act only if your action could become "
        "universal law. An action is good or bad based on clear rules and "
        "the intentions behind it, not merely its consequences."
    ),
    "strengths": [
        "Provides firm moral boundaries that cannot be overridden by outcomes",
        "Respects individual dignity — people are ends, never merely means",
        "Creates predictable, trustworthy social structures",
    ],
    "weaknesses": [
        "Rigid rules can produce absurd outcomes in edge cases",
        "Does not account well for conflicting duties",
        "Can be used to justify inaction when action is needed",
    ],
    "tech_application": (
        "Tech needs rules. Parler demonstrated what happens when content "
        "moderation rules are removed: the universal law of 'post whatever "
        "you want, even if dangerous' resulted in the January 6th insurrection. "
        "Kant would say such speech is illogical because society cannot run "
        "under constant threat."
    ),
}

EXISTENTIALISM = {
    "name": "Existentialism",
    "key_thinker": "Jean-Paul Sartre, Søren Kierkegaard",
    "core_idea": (
        "We are our choices. Individuals have agency over their actions and "
        "must find purpose through authentic living. Living by someone else's "
        "rules puts us in a position of 'bad faith.'"
    ),
    "strengths": [
        "Emphasizes personal responsibility and authentic choice",
        "Encourages critical examination of inherited assumptions",
        "Values the individual's unique perspective and agency",
    ],
    "weaknesses": [
        "The 'paradox of choice' can be paralyzing",
        "Lack of external guidelines can lead to existential crisis",
        "Does not provide clear guidance for collective action",
    ],
    "tech_application": (
        "Everything we build contains a piece of us that reflects our biases, "
        "opinions, thoughts, and morals. Facebook was constructed as a public "
        "square but critics argue it now operates in 'bad faith' — serving "
        "profits and ads rather than its stated purpose."
    ),
}

EGOTISM_AND_ALTRUISM = {
    "name": "Egotism and Altruism",
    "key_thinker": "Various (psychological and ethical egotism traditions)",
    "core_idea": (
        "Altruism is selfless concern for others' welfare. Egotism views "
        "self-interest as the foundation of morality. Psychological egotism "
        "holds that people always act from self-interest; ethical egotism "
        "holds that it is always right to do so."
    ),
    "tech_application": (
        "Tech can be filled with the idea that 'they are doing it, so it's "
        "ok for us to do it as well.' The majority is not necessarily right. "
        "We must be conscious of our intentions and foundations, otherwise "
        "our technology can get away from us. Develop altruistically — "
        "because it's the right thing to do."
    ),
}

LEGALISM = {
    "name": "Legalism",
    "key_thinker": "Various legal philosophers, Joel Feinberg",
    "core_idea": (
        "Strict adherence to rules, distinguishing between the 'letter of "
        "the law' (literal reading) and the 'spirit of the law' (intent). "
        "Following both helps achieve holistic order. Feinberg argues that "
        "the law should intervene only when conduct causes harm to others."
    ),
    "tech_application": (
        "Some letters of the law can't keep up with tech progress, so "
        "understanding the spirit of the law helps us work through rapid "
        "change. Feinberg warns that some groups won't see potential harm, "
        "so we must draw in the full scope of how offenses affect people."
    ),
}

# ---------------------------------------------------------------------------
# 2. TODD MAY'S DECENCY PRINCIPLE (Course Central Framework)
# ---------------------------------------------------------------------------

DECENCY_PRINCIPLE = {
    "name": "Todd May's Decency Principle",
    "key_thinker": "Todd May",
    "source": "A Decent Life: Morality for the Rest of Us (2019)",
    "core_idea": (
        "Individuals have a moral obligation to treat others with respect "
        "and consideration, recognizing the inherent dignity and worth of "
        "every person. Decency is not mere absence of harm but active "
        "orientation toward dignity, autonomy, and well-being."
    ),
    "applications": {
        "decency_to_self": (
            "Identify and respect who you are. Treat yourself with respect "
            "and kindness. Maintain clear goals, values, and beliefs. Show "
            "yourself grace. Avoid the slippery slope of over-alienation "
            "(Marx) where you lose yourself in the tools you create."
        ),
        "decency_to_others": (
            "Treat others with respect and kindness. Recognize inherent "
            "value and dignity of every person. Act fairly, justly, and "
            "respectfully. Help others in need. Practice empathy (not just "
            "sympathy) — see the world through their eyes."
        ),
        "decency_to_non_humans": (
            "Our actions impact non-humans (animals, environment, AI "
            "systems). Individual relationships matter. Extrapolate from "
            "your framework of decency to self and community. The way we "
            "treat digital counterparts reflects on us."
        ),
        "decency_to_the_world": (
            "Decency at scale. AI amplifies either benefits or damage. "
            "Apply a 'light touch' — stewardship rather than domination. "
            "Overcome short-term thinking; consider long-term consequences. "
            "Act for the ecosystem and ourselves together."
        ),
    },
    "key_warning": (
        "We cannot operate in ethical absolutes. Moral decision-making "
        "involves complex, nuanced considerations. The moral landscape "
        "evolves as new technologies and social norms emerge. Being "
        "all-selfish or all-giving is unrealistic; balance is key."
    ),
}

# ---------------------------------------------------------------------------
# 3. FIVE PRINCIPLES OF AI ETHICS (Floridi & Cowls)
# ---------------------------------------------------------------------------

FIVE_PRINCIPLES = {
    "source": "Floridi & Cowls (2019), 'A Unified Framework of Five Principles for AI in Society'",
    "principles": {
        "beneficence": {
            "title": "Beneficence: Promoting Well-Being, Preserving Dignity, Sustaining the Planet",
            "definition": (
                "AI should be developed to promote the welfare and well-being "
                "of individuals and society, identify and address social problems, "
                "and improve quality of life."
            ),
        },
        "non_maleficence": {
            "title": "Non-Maleficence: Privacy, Security, and Capability Caution",
            "definition": (
                "AI should avoid causing harm or suffering. Minimize potential "
                "for misuse or abuse. Respect rights including privacy and "
                "freedom from discrimination."
            ),
        },
        "autonomy": {
            "title": "Autonomy: The Power to Decide",
            "definition": (
                "AI should respect individuals' ability to make their own "
                "decisions and act freely. Avoid creating dependencies on "
                "AI systems. Enable informed, well-considered decisions."
            ),
        },
        "justice": {
            "title": "Justice: Promoting Prosperity, Preserving Solidarity, Avoiding Unfairness",
            "definition": (
                "AI should be fair and unbiased, avoiding discrimination. "
                "Promote the common good and fair distribution of benefits "
                "and burdens."
            ),
        },
        "explicability": {
            "title": "Explicability: Intelligibility and Accountability",
            "definition": (
                "AI should be transparent and explainable. People should "
                "understand how and why it makes decisions. Promote trust "
                "and enable accountability."
            ),
        },
    },
}

# ---------------------------------------------------------------------------
# 4. AI-SPECIFIC ETHICAL FRAMEWORKS & DECLARATIONS
# ---------------------------------------------------------------------------

ASILOMAR_PRINCIPLES = {
    "name": "Asilomar AI Principles (2017)",
    "summary": (
        "23 principles covering research, values, long-term issues, and "
        "governance. Key tenets include: beneficial intelligence as the goal, "
        "failure transparency, judicial transparency, value alignment, "
        "human values, personal privacy, shared benefit, human control, "
        "non-subversion, and avoidance of AI arms races."
    ),
}

MONTREAL_DECLARATION = {
    "name": "Montreal Declaration of Responsible AI (2018)",
    "summary": (
        "10 principles: well-being, respect for autonomy, protection of "
        "privacy, solidarity, democratic participation, equity, diversity "
        "inclusion, prudence, responsibility, and sustainable development."
    ),
}

PARTNERSHIPS_ON_AI = {
    "name": "Partnerships on AI Tenets",
    "summary": (
        "Founded by Google, Amazon, Facebook, and Microsoft in 2016. "
        "Tenets include: benefit and empower as many people as possible, "
        "educate and engage the public, commit to open research, ensure "
        "accountability to stakeholders, protect privacy and security, "
        "and create a culture of cooperation and trust."
    ),
}

OECD_AI_PRINCIPLES = {
    "name": "OECD AI Principles (2024)",
    "summary": (
        "Five principles for trustworthy AI: (1) inclusive growth and "
        "well-being, (2) human rights, democratic values, fairness, privacy, "
        "and autonomy, (3) transparency and explainability, (4) robustness, "
        "security, and safety, and (5) accountability."
    ),
}

# ---------------------------------------------------------------------------
# 5. THOUGHT EXPERIMENTS & CASE STUDIES
# ---------------------------------------------------------------------------

THOUGHT_EXPERIMENTS = {
    "trolley_problem": {
        "name": "The Trolley Problem",
        "description": (
            "An out-of-control trolley will kill five workers. You can "
            "pull a lever to divert it, killing one worker instead. "
            "Variant: push someone off a bridge to stop the trolley."
        ),
        "ethical_tensions": "Utilitarian calculus vs. active commission of harm",
    },
    "ship_of_theseus": {
        "name": "The Ship of Theseus",
        "description": (
            "A ship's planks are replaced one by one. Is it still the same "
            "ship? If the old planks are reassembled, which is the 'real' ship?"
        ),
        "ethical_tensions": (
            "Identity metaphysics. Technology undergoes the same 'rot and "
            "replace' process. The ethical framework may be the only thing "
            "that persists of the original technology."
        ),
    },
    "ring_of_gyges": {
        "name": "The Ring of Gyges (Plato)",
        "description": (
            "A shepherd discovers a ring granting invisibility. Would you "
            "act morally if you could act with complete impunity?"
        ),
        "ethical_tensions": (
            "Power without accountability. AI systems can give actors "
            "effective 'invisibility' — acting at scale without facing "
            "consequences. Who pulls the strings matters."
        ),
    },
    "drowning_person": {
        "name": "The Drowning Person",
        "description": (
            "You see someone drowning. Do you risk yourself to save them? "
            "Would your answer change if you were wearing a $1000 suit?"
        ),
        "ethical_tensions": (
            "Cost of ethical action. We may face choices about whether to "
            "use AI to address problems even when it involves risk or cost."
        ),
    },
    "rawls_original_position": {
        "name": "Rawls' Original Position (Veil of Ignorance)",
        "description": (
            "Imagine designing society's principles without knowing your "
            "own position in it. What rules would you choose?"
        ),
        "ethical_tensions": (
            "Objectivity in design. If AI designers didn't know whether "
            "they'd be users or subjects of the system, how would they "
            "design it differently?"
        ),
    },
}

# ---------------------------------------------------------------------------
# 6. KEY COURSE CONCEPTS
# ---------------------------------------------------------------------------

KEY_CONCEPTS = {
    "technology_is_amoral": (
        "Technology in itself is inherently amoral — it just exists and "
        "executes actions. However, the intent in which it is created and "
        "the way it is used are practiced by humans. A human should not "
        "hide behind the excuse of 'the robot did it.'"
    ),
    "hype_cycle": (
        "Gartner's Hype Cycle: Innovation Trigger → Peak of Inflated "
        "Expectations → Trough of Disillusionment → Slope of Enlightenment "
        "→ Plateau of Productivity. The slope of enlightenment is when we "
        "understand practical uses and can think about consequences."
    ),
    "alienation": (
        "Part of ourselves is put into the tools we create (Marx's theory). "
        "Creating something costs us labor, energy, creativity. There is a "
        "tipping point where we spend so much of ourselves in tech that we "
        "don't enjoy the benefits anymore."
    ),
    "human_centered_design": (
        "Three factors: Desirability (do people want it?), Feasibility "
        "(can we build it?), and Viability (is it sustainable?). All must "
        "be present, framed from the self first, then expanding outward."
    ),
    "circle_of_community": (
        "Concentric circles: my home/family → my neighborhood/community "
        "→ my state/nation/culture → the wider world. Actions should be "
        "fair and respectful to all within these circles."
    ),
    "empathy_vs_sympathy": (
        "Sympathy recognizes another's pain; empathy feels it. In design "
        "thinking, we empathize with the user — understanding they have a "
        "problem and working to fix it. This leads to better experiences."
    ),
    "effective_altruism": (
        "Identify the most effective ways to address global problems and "
        "allocate resources to maximize positive impact. AI can process "
        "tremendous data to forecast and address global challenges."
    ),
}


def get_all_frameworks_summary() -> str:
    """Return a condensed summary of all frameworks for use in system prompts."""
    return """
FOUNDATIONAL ETHICAL FRAMEWORKS:

1. UTILITARIANISM (Bentham, Mill): Maximize pleasure, minimize pain for the
   greatest number. Outcomes matter most. Risk: dehumanizing individuals.

2. DEONTOLOGY (Kant): Act only as you'd want everyone to act (categorical
   imperative). Rules and intentions matter, not just outcomes. People are
   ends, not means.

3. EXISTENTIALISM (Sartre, Kierkegaard): We are our choices. Live
   authentically. 'Bad faith' = living by others' rules. Everything we
   build reflects our biases.

4. EGOTISM & ALTRUISM: Tension between self-interest and selfless concern.
   Psychological egotism says all acts are self-interested. Develop
   altruistically — because it's the right thing to do.

5. LEGALISM (Feinberg): Letter vs. spirit of the law. Both needed for
   holistic order. Law should intervene only when conduct harms others.

6. TODD MAY'S DECENCY PRINCIPLE: Moral obligation to treat all with respect
   and consideration, recognizing inherent dignity. Applied to: self,
   others, non-humans, and the world. Not absence of harm but active
   orientation toward dignity. No ethical absolutes — balance is key.

FIVE PRINCIPLES OF AI ETHICS (Floridi & Cowls):
- Beneficence (do good), Non-maleficence (do no harm), Autonomy (respect
  choice), Justice (fairness), Explicability (transparency/accountability).

AI-SPECIFIC DECLARATIONS:
- Asilomar (23 principles), Montreal Declaration (10 principles),
  Partnerships on AI, OECD AI Principles.

KEY CONCEPTS: Technology is amoral but human intent is not. Hype Cycle
governs adoption and regulation timing. Human-Centered Design requires
desirability + feasibility + viability. Circle of Community expands from
self outward. Empathy (not mere sympathy) drives ethical design.

THOUGHT EXPERIMENTS: Trolley Problem (utilitarian calculus vs. active harm),
Ship of Theseus (identity & technology lifecycle), Ring of Gyges (power
without accountability), Drowning Person (cost of ethical action), Rawls'
Veil of Ignorance (objective design).
"""
