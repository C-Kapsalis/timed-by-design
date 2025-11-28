"""
Human Design Insights Module
Comprehensive interpretations for all aspects of Human Design
"""

# ==================== TYPE INSIGHTS ====================

TYPE_INSIGHTS = {
    "Generator": {
        "description": """
Generators are the life force of the planet, comprising about 37% of the population. You have a defined Sacral center, 
giving you sustainable, regenerative energy when you're doing work you love. Your aura is open and enveloping, 
drawing life to you. You're designed to master something and find deep satisfaction in your work.
        """,
        "strengths": [
            "Sustainable energy for work you love",
            "Powerful gut instinct (Sacral response)",
            "Ability to master skills through dedication",
            "Magnetic aura that attracts opportunities",
            "Deep satisfaction when correctly engaged"
        ],
        "challenges": [
            "Tendency to initiate rather than respond",
            "Saying yes when your gut says no",
            "Frustration when stuck in wrong work",
            "Not waiting for the right opportunities",
            "Ignoring your body's wisdom"
        ],
        "key_practice": """
Practice waiting to respond before committing. When opportunities come, check your gut response - 
that 'uh-huh' (yes) or 'uhn-uhn' (no). Your body knows before your mind. 
Start with small decisions and build trust in your Sacral authority.
        """,
        "strategy_detail": """
'Wait to Respond' means letting life come to you rather than chasing it. This doesn't mean being passive - 
stay engaged with life so there's something to respond to. When someone asks you something or life presents 
an opportunity, notice your body's immediate response. That's your truth.
        """
    },
    
    "Manifesting Generator": {
        "description": """
Manifesting Generators are multi-passionate powerhouses, about 33% of the population. You have the sustainable 
energy of a Generator plus a connection from a motor to the Throat, giving you the ability to move quickly 
and do multiple things. You're here to find shortcuts, skip steps, and be efficient.
        """,
        "strengths": [
            "Incredible energy and speed",
            "Multi-passionate nature - can do many things",
            "Ability to find shortcuts and efficiencies",
            "Powerful gut + motor energy combination",
            "Quick to master new skills"
        ],
        "challenges": [
            "Starting things before responding",
            "Frustration when slowed down",
            "Skipping important steps",
            "Difficulty finishing what you start",
            "Not informing others before acting"
        ],
        "key_practice": """
Honor your multi-passionate nature while still waiting to respond. When your gut says yes, 
inform those who will be impacted before you spring into action. It's okay to change direction - 
that's part of your design. Trust your non-linear path.
        """,
        "strategy_detail": """
'Wait to Respond, then Inform' combines Generator and Manifestor strategies. Wait for your Sacral response, 
then before you leap into action, let people know what you're doing. This reduces resistance and anger. 
Your path may look chaotic to others but makes perfect sense to you.
        """
    },
    
    "Manifestor": {
        "description": """
Manifestors are the initiators, about 8% of the population. You have a motor connected to the Throat 
without a defined Sacral, giving you the power to initiate and impact. Your aura is closed and repelling - 
not to push people away, but to maintain your independence. You're here to start things and make an impact.
        """,
        "strengths": [
            "Ability to initiate and start new things",
            "Powerful impact on others",
            "Independence and self-sufficiency",
            "Visionary capacity",
            "Natural leadership presence"
        ],
        "challenges": [
            "Anger when controlled or slowed down",
            "Others may find you intimidating",
            "Not informing leads to resistance",
            "Difficulty with sustainable energy",
            "Feeling isolated or misunderstood"
        ],
        "key_practice": """
Practice informing before you act. Not asking permission, but letting people know what you're about to do. 
This simple practice dramatically reduces the resistance you encounter. Rest when you need to - 
you're not designed for sustained work like Generators.
        """,
        "strategy_detail": """
'Inform before Acting' is about reducing resistance. Your aura naturally creates fear in others because 
they can feel your power but can't penetrate your closed aura. When you inform, you bring people into your 
process and create allies instead of obstacles.
        """
    },
    
    "Projector": {
        "description": """
Projectors are the guides and seers, about 20% of the population. Without a defined Sacral and no motor 
to Throat, you're designed to guide and manage energy, not generate it. Your focused, penetrating aura 
can see deeply into others. You're here to be recognized and invited for your wisdom.
        """,
        "strengths": [
            "Ability to see and understand others deeply",
            "Natural guidance and management skills",
            "Wisdom that comes from studying systems",
            "Success when properly recognized",
            "Efficiency - working smarter not harder"
        ],
        "challenges": [
            "Bitterness when not recognized or invited",
            "Over-giving energy trying to be seen",
            "Working like a Generator and burning out",
            "Waiting for invitations can feel passive",
            "Not knowing your own energy limits"
        ],
        "key_practice": """
Focus on being recognized for who you are, not what you do. Wait for invitations for big life decisions 
(career, relationships, where to live). Study what fascinates you - your mastery attracts the right 
invitations. Rest more than you think you need.
        """,
        "strategy_detail": """
'Wait for the Invitation' doesn't mean waiting for permission for everything. It's specifically for 
the big areas: love, career, where you live, and your purpose. In daily life, wait to be asked before 
offering guidance. When you're invited, your wisdom lands perfectly.
        """
    },
    
    "Reflector": {
        "description": """
Reflectors are the rarest type, about 1% of the population. With no defined centers, you're completely 
open to the world around you. You sample and reflect the health of your community. Your openness is your 
gift - you can experience life in ways others cannot.
        """,
        "strengths": [
            "Ability to read and reflect communities",
            "Potential for deep wisdom about others",
            "Unique perspective on life",
            "Natural objectivity",
            "Gift of surprise and wonder"
        ],
        "challenges": [
            "Disappointment when communities are unhealthy",
            "Difficulty knowing who you truly are",
            "Taking in too much from others",
            "Pressure to decide quickly",
            "Finding the right environment"
        ],
        "key_practice": """
Wait a full lunar cycle (28 days) before making major decisions. This allows you to sample all the 
different energies and perspectives. Your environment is everything - find places and people that 
feel good to reflect. Embrace your uniqueness.
        """,
        "strategy_detail": """
'Wait a Lunar Cycle' honors your connection to the moon. Each day the moon activates different gates, 
giving you a different experience. By waiting 28 days, you've experienced the full spectrum and can 
make decisions from a place of true clarity.
        """
    }
}

def get_type_insights(hd_type):
    return TYPE_INSIGHTS.get(hd_type, TYPE_INSIGHTS["Generator"])


# ==================== AUTHORITY INSIGHTS ====================

AUTHORITY_INSIGHTS = {
    "Emotional": {
        "description": """
With Emotional Authority, your Solar Plexus center is defined, creating an emotional wave that moves 
through highs and lows. There is no truth in the moment for you - clarity comes with time. You're 
designed to ride your wave and only decide when you reach emotional neutrality.
        """,
        "how_to_use": [
            "Never make decisions in emotional highs or lows",
            "Sleep on important decisions - multiple times if needed",
            "Notice your emotional wave patterns over days/weeks",
            "Say 'Let me get back to you' to give yourself time",
            "Check in with yourself at different points in your wave"
        ],
        "warning": """
Making decisions when you're emotionally up will lead to regret when you come down. 
Making decisions when you're emotionally down will cause you to miss opportunities. 
Wait for the middle ground where you can see both sides clearly.
        """
    },
    
    "Sacral": {
        "description": """
With Sacral Authority, you have direct access to your body's wisdom through gut responses. 
Your Sacral speaks in sounds - 'uh-huh' (yes), 'uhn-uhn' (no), or silence (not now). 
This is your most reliable guide to correct decisions.
        """,
        "how_to_use": [
            "Ask yourself yes/no questions to get clear responses",
            "Have others ask you questions and notice your gut reaction",
            "Pay attention to what lights you up vs. drains you",
            "Trust your immediate response before your mind kicks in",
            "Practice with small decisions to build trust"
        ],
        "warning": """
Your mind will try to override your Sacral response with logic and reasoning. 
The Sacral knows before the mind. If you have to convince yourself, it's not a yes.
        """
    },
    
    "Splenic": {
        "description": """
With Splenic Authority, you have access to the oldest survival awareness. Your Spleen speaks 
once, in the moment, as a quiet intuitive hit. It's about survival, health, and what's safe 
for you right now.
        """,
        "how_to_use": [
            "Trust your first instinct - it won't repeat",
            "Notice spontaneous knowing about people and situations",
            "Pay attention to body sensations - chills, gut feelings",
            "Act on intuition in the moment - don't wait",
            "Your intuition is about NOW, not the future"
        ],
        "warning": """
The Spleen speaks only once and very quietly. If you miss it or override it, the moment passes. 
Your mind will try to rationalize later, but the intuition was correct. Learn to trust your 
first hit, even when it doesn't make logical sense.
        """
    },
    
    "Ego": {
        "description": """
With Ego Authority, your Heart/Ego center is defined and connected to your Throat. 
Your decisions need to come from willpower and personal desire. Ask yourself: 
'Do I want this? Is my heart in it?'
        """,
        "how_to_use": [
            "Make commitments only when your heart is truly in it",
            "Listen for 'I want' or 'I don't want' in your truth",
            "Your willpower needs to be engaged for success",
            "Don't make promises you can't keep - it depletes you",
            "Honor what YOU want, not what others expect"
        ],
        "warning": """
The Ego center is about willpower, but it's not sustainable like Sacral energy. 
You need rest. Making commitments from 'should' rather than 'want' will exhaust you 
and lead to broken promises.
        """
    },
    
    "Self-Projected": {
        "description": """
With Self-Projected Authority, your G Center is connected to your Throat. 
Your truth emerges through speaking and hearing yourself. You need to talk things 
through with trusted people who can listen without advising.
        """,
        "how_to_use": [
            "Talk through decisions with trusted friends",
            "Pay attention to what you hear yourself saying",
            "Your direction becomes clear when you voice it",
            "Find people who listen without trying to influence",
            "Notice what feels like 'you' when you speak"
        ],
        "warning": """
You're not looking for advice or opinions from others. You need sounding boards 
who can listen while you discover your own truth. Be careful not to take on 
others' perspectives as your own.
        """
    },
    
    "Mental": {
        "description": """
With Mental (Outer) Authority, neither your Sacral, Spleen, Solar Plexus, Heart, nor G center 
is defined. Your authority is actually external - it comes from talking with others and 
being in the right environment.
        """,
        "how_to_use": [
            "Discuss decisions with many different people",
            "Pay attention to your environment - it shapes your decisions",
            "Notice what consistent themes emerge in conversations",
            "Don't rely on any single person's input",
            "Your body needs to feel good in the environment of the decision"
        ],
        "warning": """
You have incredible mental gifts but shouldn't use your mind as your authority. 
Your insights are for others, not yourself. Rely on your extended network and 
environment to guide your personal decisions.
        """
    },
    
    "Lunar": {
        "description": """
As a Reflector with Lunar Authority, you're connected to the lunar cycle. 
Wait 28 days before making major decisions, allowing yourself to experience 
all the different energies the moon brings.
        """,
        "how_to_use": [
            "Mark your calendar 28 days ahead for big decisions",
            "Journal daily about how you feel regarding the decision",
            "Notice how your perspective shifts throughout the month",
            "Seek out healthy, supportive environments",
            "Trust the clarity that comes after a full cycle"
        ],
        "warning": """
You're constantly sampling everyone else's energy. Major decisions made quickly 
may be based on someone else's energy, not yours. The lunar cycle gives you 
access to YOUR truth, not the reflected truth of others.
        """
    }
}

def get_authority_insights(authority):
    return AUTHORITY_INSIGHTS.get(authority, AUTHORITY_INSIGHTS["Sacral"])


# ==================== PROFILE INSIGHTS ====================

PROFILE_INSIGHTS = {
    "1/3": {
        "description": "The Investigator/Martyr combines deep research with experiential learning. You need a solid foundation before you can relax, and you learn through trial and error.",
        "life_theme": "Building secure foundations through personal experience and research",
        "learning_style": "Deep investigation combined with hands-on experimentation - learning what works by discovering what doesn't"
    },
    "1/4": {
        "description": "The Investigator/Opportunist needs deep foundations and shares through their network. Your security comes from expertise, and opportunities come through people you know.",
        "life_theme": "Becoming an expert and sharing knowledge through your close network",
        "learning_style": "Thorough research that you then share with your established community"
    },
    "2/4": {
        "description": "The Hermit/Opportunist has natural talents that others recognize. You need alone time to develop your gifts, and your network calls them out of you.",
        "life_theme": "Being called out to share your natural genius with those who recognize it",
        "learning_style": "Natural absorption during hermit time, activated through relationships"
    },
    "2/5": {
        "description": "The Hermit/Heretic is called out to save the day. You have natural gifts that others project solutions onto. You need solitude to recharge.",
        "life_theme": "Being universally called upon to provide practical solutions",
        "learning_style": "Developing natural talents in private, then sharing universally when called"
    },
    "3/5": {
        "description": "The Martyr/Heretic learns through trial and error and has a reputation for solving problems. Your life is about discovering what works and sharing it.",
        "life_theme": "Learning through experience to become a universally helpful problem-solver",
        "learning_style": "Hands-on experimentation that becomes wisdom for others"
    },
    "3/6": {
        "description": "The Martyr/Role Model lives a three-part life. Until 30, you experiment. From 30-50, you observe. After 50, you become a wise role model.",
        "life_theme": "Moving from experiential learning to objective wisdom to role modeling",
        "learning_style": "Trial and error in youth, observation in middle life, embodied wisdom later"
    },
    "4/6": {
        "description": "The Opportunist/Role Model influences through their network and becomes a role model over time. Your relationships are key to your impact.",
        "life_theme": "Building networks in youth that support your role model phase later",
        "learning_style": "Learning through relationships, embodying wisdom after life experience"
    },
    "4/1": {
        "description": "The Opportunist/Investigator needs both community and a solid foundation. Your fixed nature means you need to investigate before committing.",
        "life_theme": "Building fixed foundations shared through loyal relationships",
        "learning_style": "Deep research combined with learning through your network"
    },
    "5/1": {
        "description": "The Heretic/Investigator is seen as a problem solver with solid foundations. Others project savior qualities onto you - make sure you have the expertise to back it up.",
        "life_theme": "Delivering practical solutions built on thorough research",
        "learning_style": "Deep investigation that prepares you for universal projection"
    },
    "5/2": {
        "description": "The Heretic/Hermit is called out to save the day with their natural gifts. You need significant alone time to recharge from the projections.",
        "life_theme": "Answering universal calls while protecting your hermit nature",
        "learning_style": "Natural talents that emerge through being called out, balanced with solitude"
    },
    "6/2": {
        "description": "The Role Model/Hermit lives a three-part life with natural talents. You need solitude, and your life trajectory moves toward objective wisdom.",
        "life_theme": "Developing natural gifts through life experience to become a role model",
        "learning_style": "Natural absorption in solitude, life experience creating wisdom"
    },
    "6/3": {
        "description": "The Role Model/Martyr combines life phases with trial and error. Your optimism is tested through experience, eventually becoming wise example.",
        "life_theme": "Learning through experience across life phases to become an authentic role model",
        "learning_style": "Experiential learning throughout life's three phases"
    }
}

def get_profile_insights(profile):
    return PROFILE_INSIGHTS.get(profile, {
        "description": "Your unique profile combines different life themes.",
        "life_theme": "Discovering your unique path through life",
        "learning_style": "Your own unique way of learning and growing"
    })


# ==================== DEFINITION INSIGHTS ====================

DEFINITION_INSIGHTS = {
    "Single Definition": {
        "description": "All your defined centers are connected. You have a consistent, self-contained energy.",
        "meaning": "You don't need others to feel complete. You process internally and are relatively fixed in your nature.",
        "gift": "Self-sufficiency and consistency",
        "challenge": "May not understand why others need more processing time"
    },
    "Split Definition": {
        "description": "You have two separate areas of definition that need bridging.",
        "meaning": "You may seek others who 'bridge' your split, completing your circuit. This creates attraction.",
        "gift": "Natural ability to connect with others who complement you",
        "challenge": "May feel incomplete alone, or become dependent on bridging"
    },
    "Triple Split": {
        "description": "Three separate areas of definition create complex bridging needs.",
        "meaning": "You benefit from multiple connections to bring all parts of yourself together.",
        "gift": "Ability to connect with many different types of people",
        "challenge": "May need several people or time to feel whole"
    },
    "Quadruple Split": {
        "description": "Four separate areas of definition require extensive bridging.",
        "meaning": "You need time and different people to feel integrated. Take time for major decisions.",
        "gift": "Deep understanding of human diversity",
        "challenge": "Processing can take significant time and varied input"
    },
    "No Definition": {
        "description": "As a Reflector, you have no definition - all centers are open.",
        "meaning": "You sample and reflect the energy around you. Your environment is everything.",
        "gift": "Unique perspective, ability to see community health",
        "challenge": "Finding your own identity amidst all the sampling"
    }
}

def get_definition_insights(definition):
    return DEFINITION_INSIGHTS.get(definition, DEFINITION_INSIGHTS["Single Definition"])


# ==================== CENTER INSIGHTS ====================

CENTER_INSIGHTS = {
    "Head": {
        "description": "The Head center is a pressure center for inspiration and mental questions. It's about the pressure to understand the mystery of life.",
        "defined_meaning": "You have a consistent way of being inspired and questioning. Your mental pressure is reliable and doesn't need external stimulation.",
        "open_meaning": "You take in and amplify others' questions and inspirations. You can become overwhelmed by thinking about things that aren't important to you.",
        "not_self_question": "Am I trying to answer everyone else's questions?",
        "wisdom": "When aligned, you can discern which questions are worth pursuing and which are just mental noise."
    },
    "Ajna": {
        "description": "The Ajna center is about mental processing, conceptualization, and opinions. It's how we make sense of information.",
        "defined_meaning": "You have a fixed way of processing and conceptualizing. Your opinions and mental frameworks are consistent.",
        "open_meaning": "You can see and understand all perspectives. You're not fixed to one way of thinking.",
        "not_self_question": "Am I pretending to be certain about things to fit in?",
        "wisdom": "When aligned, you have the gift of seeing all sides of any issue and not being attached to being right."
    },
    "Throat": {
        "description": "The Throat center is about communication, manifestation, and action. Everything manifests through the Throat.",
        "defined_meaning": "You have consistent access to expression and manifestation. Your voice and ability to take action is reliable.",
        "open_meaning": "You may feel pressure to speak or attract attention. Your voice and expression varies based on who you're with.",
        "not_self_question": "Am I talking just to get attention or be noticed?",
        "wisdom": "When aligned, you know when to speak and when to be silent. You can recognize true voice from noise."
    },
    "G": {
        "description": "The G Center (Identity Center) is about love, direction, and identity. It's your internal GPS and sense of self.",
        "defined_meaning": "You have a fixed sense of identity and direction. You know who you are and where you're going.",
        "open_meaning": "Your identity and direction are fluid. You experience life through many different identities and directions.",
        "not_self_question": "Am I desperately searching for love and direction?",
        "wisdom": "When aligned, you become wise about identity and love, seeing that you don't need to be fixed to be valuable."
    },
    "Heart": {
        "description": "The Heart/Ego center is about willpower, self-worth, and the material world. It's about proving and ego.",
        "defined_meaning": "You have consistent willpower and natural self-worth. You can make promises and keep them.",
        "open_meaning": "Your willpower comes and goes. You have nothing to prove. Your worth is not about what you do.",
        "not_self_question": "Am I trying to prove my worth or make promises I can't keep?",
        "wisdom": "When aligned, you understand that you don't need to prove anything. Worth isn't earned - it just is."
    },
    "Sacral": {
        "description": "The Sacral center is the life force and work force. It's about sustainable energy, sexuality, and response.",
        "defined_meaning": "You have sustainable, regenerative energy. You're designed for work you love and have strong gut responses.",
        "open_meaning": "You don't have consistent life force energy. You're not here to work like Generators. Your energy is borrowed.",
        "not_self_question": "Am I not knowing when enough is enough?",
        "wisdom": "When aligned, you become wise about work and energy, knowing exactly how much is correct for you."
    },
    "Spleen": {
        "description": "The Spleen center is about intuition, survival, health, and well-being. It's our oldest awareness center.",
        "defined_meaning": "You have consistent access to intuition and immune response. Your body knows what's safe.",
        "open_meaning": "You take in and amplify others' fears and health states. You can become extra sensitive.",
        "not_self_question": "Am I holding on to things that aren't good for me?",
        "wisdom": "When aligned, you can deeply attune to wellness and become wise about what's truly healthy."
    },
    "Solar Plexus": {
        "description": "The Solar Plexus is the emotional center. It operates in a wave and is also a motor and awareness center.",
        "defined_meaning": "You have emotional waves that need to be honored. There's no truth in the moment - clarity comes with time.",
        "open_meaning": "You amplify and take in others' emotions. You can feel others deeply and become emotionally wise.",
        "not_self_question": "Am I avoiding truth and confrontation to keep the peace?",
        "wisdom": "When aligned, you become wise about emotions, able to discern your feelings from others' and not be overwhelmed."
    },
    "Root": {
        "description": "The Root center is a pressure center and motor. It's about adrenaline, stress, and the pressure to evolve.",
        "defined_meaning": "You have consistent access to adrenaline energy. You can handle stress and pressure reliably.",
        "open_meaning": "You amplify and take in pressure from others. You may rush to be free of the pressure.",
        "not_self_question": "Am I in a hurry to get things done so I can be free?",
        "wisdom": "When aligned, you become wise about pressure, knowing which pressures are yours and which to release."
    }
}

def get_center_insights(center, is_defined):
    return CENTER_INSIGHTS.get(center, {
        "description": "This center represents a key aspect of your being.",
        "defined_meaning": "You have consistent access to this energy.",
        "open_meaning": "You are sensitive to this energy in others.",
        "not_self_question": "Am I living correctly with this energy?",
        "wisdom": "You can become wise about this aspect of life."
    })


# ==================== CHANNEL INSIGHTS ====================

CHANNEL_INSIGHTS = {
    "1-8": {
        "description": "The Channel of Inspiration connects the G Center to the Throat. It's about creative self-expression and inspiring others through your unique individuality.",
        "gift": "Natural creative expression and the ability to inspire others just by being yourself",
        "shadow": "Creating for attention rather than authentic expression"
    },
    "2-14": {
        "description": "The Channel of the Beat connects the G Center to the Sacral. It's about empowerment through direction and work that's aligned with your identity.",
        "gift": "Deeply empowering others through your direction and life force",
        "shadow": "Working on things that aren't aligned with who you truly are"
    },
    "3-60": {
        "description": "The Channel of Mutation connects the Sacral to the Root. It's about bringing change and mutation through creative energy.",
        "gift": "Ability to handle and bring necessary change and evolution",
        "shadow": "Impatience with the process of mutation, wanting to force change"
    },
    "4-63": {
        "description": "The Channel of Logic connects the Ajna to the Head. It's about logical thinking and the mental pressure to understand.",
        "gift": "Powerful logical mind capable of seeing patterns and solving problems",
        "shadow": "Mental anxiety and doubt, questioning everything to exhaustion"
    },
    "5-15": {
        "description": "The Channel of Rhythm connects the Sacral to the G Center. It's about flowing with the rhythms of life and nature.",
        "gift": "Natural attunement to life's rhythms, ability to flow with timing",
        "shadow": "Forcing things out of their natural rhythm"
    },
    "6-59": {
        "description": "The Channel of Intimacy connects the Solar Plexus to the Sacral. It's about emotional and sexual intimacy, breaking down barriers.",
        "gift": "Deep capacity for intimacy and emotional connection",
        "shadow": "Intimacy without emotional clarity, boundary issues"
    },
    "7-31": {
        "description": "The Channel of the Alpha connects the G Center to the Throat. It's about democratic leadership and leading by example.",
        "gift": "Natural leadership that inspires others toward the future",
        "shadow": "Leading without being recognized or invited"
    },
    "9-52": {
        "description": "The Channel of Concentration connects the Sacral to the Root. It's about focused determination and stillness in action.",
        "gift": "Incredible focus and ability to concentrate deeply",
        "shadow": "Restlessness or inability to direct focus appropriately"
    },
    "10-20": {
        "description": "The Channel of Awakening connects the G Center to the Throat. It's about authentic self-expression and awakening to your true nature.",
        "gift": "Living and expressing authentically in each moment",
        "shadow": "Losing yourself in others' expectations"
    },
    "10-34": {
        "description": "The Channel of Exploration connects the G Center to the Sacral. It's about following your own convictions with power.",
        "gift": "Powerful energy to explore and follow your own path",
        "shadow": "Using power without staying true to yourself"
    },
    "10-57": {
        "description": "The Channel of Perfected Form connects the G Center to the Spleen. It's about intuitive self-love and survival through authenticity.",
        "gift": "Intuitive knowing of what keeps you healthy and aligned",
        "shadow": "Ignoring intuition about what's good for you"
    },
    "11-56": {
        "description": "The Channel of Curiosity connects the Ajna to the Throat. It's about stimulating others through ideas and stories.",
        "gift": "Natural storyteller who stimulates minds and imaginations",
        "shadow": "Telling stories that distract from truth"
    },
    "12-22": {
        "description": "The Channel of Openness connects the Throat to the Solar Plexus. It's about emotional expression and social openness.",
        "gift": "Ability to move others emotionally through expression",
        "shadow": "Expressing when emotionally unclear, creating drama"
    },
    "13-33": {
        "description": "The Channel of the Prodigal connects the G Center to the Throat. It's about witnessing and remembering experiences.",
        "gift": "Wisdom from experience that can be shared with others",
        "shadow": "Secrets or experiences that isolate rather than connect"
    },
    "16-48": {
        "description": "The Channel of the Wavelength connects the Throat to the Spleen. It's about mastery and expression of depth.",
        "gift": "Deep talent that expresses through practice and mastery",
        "shadow": "Fear of inadequacy blocking expression"
    },
    "17-62": {
        "description": "The Channel of Acceptance connects the Ajna to the Throat. It's about detailed opinions and mental expression.",
        "gift": "Ability to organize and share detailed understanding",
        "shadow": "Opinions that aren't asked for or aren't supported by experience"
    },
    "18-58": {
        "description": "The Channel of Judgment connects the Spleen to the Root. It's about the joy of correcting and perfecting patterns.",
        "gift": "Intuitive ability to see what can be improved",
        "shadow": "Criticism without invitation or joy"
    },
    "19-49": {
        "description": "The Channel of Synthesis connects the Root to the Solar Plexus. It's about emotional sensitivity to needs.",
        "gift": "Deep attunement to the needs of others and community",
        "shadow": "Emotional neediness or overwhelming others with emotion"
    },
    "20-34": {
        "description": "The Channel of Charisma connects the Throat to the Sacral. It's about immediate, direct action and expression.",
        "gift": "Charismatic ability to act and express directly",
        "shadow": "Busy-ness without direction or proper response"
    },
    "20-57": {
        "description": "The Channel of the Brainwave connects the Throat to the Spleen. It's about intuitive expression and immediate awareness.",
        "gift": "Quick, intuitive knowing expressed in the moment",
        "shadow": "Speaking without awareness or sensitivity"
    },
    "21-45": {
        "description": "The Channel of Money connects the Heart to the Throat. It's about material control and willpower.",
        "gift": "Natural ability to manage resources and direct others",
        "shadow": "Control issues or unhealthy relationship with money/power"
    },
    "23-43": {
        "description": "The Channel of Structuring connects the Throat to the Ajna. It's about genius insights and unique knowing.",
        "gift": "Breakthrough thinking and unique mental perspectives",
        "shadow": "Ideas that alienate rather than illuminate"
    },
    "24-61": {
        "description": "The Channel of Awareness connects the Ajna to the Head. It's about mental inspiration and mystery.",
        "gift": "Ability to know unknowable things through mental inspiration",
        "shadow": "Mental pressure that creates anxiety and confusion"
    },
    "25-51": {
        "description": "The Channel of Initiation connects the G Center to the Heart. It's about competitive spirit and initiation into the heart.",
        "gift": "Courage to initiate and compete for what you love",
        "shadow": "Competitive ego or shocking without purpose"
    },
    "26-44": {
        "description": "The Channel of Surrender connects the Heart to the Spleen. It's about memory and transmission of lessons.",
        "gift": "Natural salesperson who transmits truth through memory",
        "shadow": "Manipulation or selling what isn't authentic"
    },
    "27-50": {
        "description": "The Channel of Preservation connects the Sacral to the Spleen. It's about nurturing and caretaking.",
        "gift": "Powerful nurturing energy that sustains and protects",
        "shadow": "Over-responsibility or nurturing without boundaries"
    },
    "28-38": {
        "description": "The Channel of Struggle connects the Spleen to the Root. It's about the struggle to find purpose and meaning.",
        "gift": "Stubbornness and depth in finding individual purpose",
        "shadow": "Struggle that becomes suffering, fighting without purpose"
    },
    "29-46": {
        "description": "The Channel of Discovery connects the Sacral to the G Center. It's about commitment to discovery and experience.",
        "gift": "Deep capacity for embodied experience and discovery",
        "shadow": "Over-commitment or not knowing when to say no"
    },
    "30-41": {
        "description": "The Channel of Recognition connects the Solar Plexus to the Root. It's about desire and feelings that seek expression.",
        "gift": "Deep emotional desire that drives new experiences",
        "shadow": "Desire that creates unfulfilled longing"
    },
    "32-54": {
        "description": "The Channel of Transformation connects the Spleen to the Root. It's about ambition and transformation through drive.",
        "gift": "Powerful ambition and drive for transformation",
        "shadow": "Ambition without intuitive guidance"
    },
    "34-57": {
        "description": "The Channel of Power connects the Sacral to the Spleen. It's about powerful, intuitive energy.",
        "gift": "Intuitive power that knows how to survive and thrive",
        "shadow": "Power used without intuitive awareness"
    },
    "35-36": {
        "description": "The Channel of Transitoriness connects the Throat to the Solar Plexus. It's about experiencing everything once.",
        "gift": "Rich emotional experiences and adventures in life",
        "shadow": "Restlessness or emotional drama-seeking"
    },
    "37-40": {
        "description": "The Channel of Community connects the Solar Plexus to the Heart. It's about bargains and emotional support.",
        "gift": "Ability to create and nurture supportive communities",
        "shadow": "Unhealthy bargains or emotional manipulation"
    },
    "39-55": {
        "description": "The Channel of Emoting connects the Root to the Solar Plexus. It's about provocative emotions and moods.",
        "gift": "Emotional depth and the ability to move others",
        "shadow": "Moodiness without purpose, provocation without awareness"
    },
    "42-53": {
        "description": "The Channel of Maturation connects the Sacral to the Root. It's about starting and completing cycles.",
        "gift": "Ability to mature through complete cycles of experience",
        "shadow": "Starting without finishing, incomplete cycles"
    },
    "47-64": {
        "description": "The Channel of Abstraction connects the Ajna to the Head. It's about mental pressure to make sense of the past.",
        "gift": "Ability to find meaning and clarity from confusion",
        "shadow": "Mental overwhelm from trying to make sense of everything"
    }
}

def get_channel_insights(channel):
    return CHANNEL_INSIGHTS.get(channel, {
        "description": "This channel connects two centers, creating defined energy.",
        "gift": "This channel provides consistent, reliable energy in this area of life.",
        "shadow": "The shadow is the distorted expression when not living correctly."
    })


# ==================== GATE INSIGHTS (Key gates) ====================

GATE_INSIGHTS = {
    1: {"name": "Self-Expression", "theme": "The Creative", "description": "The gate of self-expression and creativity. You have a unique creative voice that wants to be expressed."},
    2: {"name": "Direction of Self", "theme": "The Receptive", "description": "The gate of direction. You have an inner knowing about direction and the driver of life."},
    3: {"name": "Ordering", "theme": "Difficulty at the Beginning", "description": "The gate of innovation and ordering. You bring mutation and change to birth something new."},
    4: {"name": "Mental Solutions", "theme": "Youthful Folly", "description": "The gate of formulization. You have the potential to find mental solutions and formulas."},
    5: {"name": "Fixed Rhythms", "theme": "Waiting", "description": "The gate of fixed rhythms. You attune to natural universal rhythms and timing."},
    6: {"name": "Friction", "theme": "Conflict", "description": "The gate of emotional intimacy. You create intimacy through emotional friction and growth."},
    7: {"name": "The Role of Self", "theme": "The Army", "description": "The gate of the role of self in interaction. You lead through your role and example."},
    8: {"name": "Contribution", "theme": "Holding Together", "description": "The gate of contribution. Your creativity contributes to the collective good."},
    9: {"name": "Focus", "theme": "Taming Power of the Small", "description": "The gate of focus and determination. You can focus deeply on details."},
    10: {"name": "Behavior of Self", "theme": "Treading", "description": "The gate of the behavior of self. You express your true nature through your behavior."},
    11: {"name": "Ideas", "theme": "Peace", "description": "The gate of ideas. You have stimulating ideas that can spark others' imagination."},
    12: {"name": "Caution", "theme": "Standstill", "description": "The gate of social caution. You express carefully when the timing is right."},
    13: {"name": "Listener", "theme": "Fellowship", "description": "The gate of the listener. You gather and hold experiences and secrets."},
    14: {"name": "Power Skills", "theme": "Great Possessing", "description": "The gate of power skills. You have resources and direction to fuel your path."},
    15: {"name": "Extremes", "theme": "Modesty", "description": "The gate of extremes. You flow with the extremes of human behavior and rhythm."},
    16: {"name": "Skills", "theme": "Enthusiasm", "description": "The gate of skills and enthusiasm. You develop mastery through experimentation."},
    17: {"name": "Opinions", "theme": "Following", "description": "The gate of opinions and mental organization. You have structured perspectives."},
    18: {"name": "Correction", "theme": "Work on What Has Been Spoilt", "description": "The gate of correction. You see what can be improved and perfected."},
    19: {"name": "Wanting", "theme": "Approach", "description": "The gate of wanting and needs. You are sensitive to the needs of others."},
    20: {"name": "Now", "theme": "Contemplation", "description": "The gate of the now and metamorphosis. You express what's alive in the present."},
    21: {"name": "Control", "theme": "Biting Through", "description": "The gate of the hunter. You control resources and move toward what you want."},
    22: {"name": "Openness", "theme": "Grace", "description": "The gate of openness and grace. You express emotion with beauty when clear."},
    23: {"name": "Assimilation", "theme": "Splitting Apart", "description": "The gate of assimilation. You translate individual knowing for others."},
    24: {"name": "Rationalization", "theme": "Return", "description": "The gate of rationalization. You revisit and make sense of inspiration."},
    25: {"name": "Innocence", "theme": "Innocence", "description": "The gate of the spirit of self. You carry universal love and innocence."},
    26: {"name": "The Egoist", "theme": "Taming Power of the Great", "description": "The gate of the egoist. You transmit and sell what you believe in."},
    27: {"name": "Caring", "theme": "Nourishment", "description": "The gate of caring. You nurture and take care of what matters to you."},
    28: {"name": "The Player", "theme": "Preponderance of the Great", "description": "The gate of the game player. You risk and struggle to find purpose."},
    29: {"name": "Saying Yes", "theme": "The Abysmal", "description": "The gate of saying yes and commitment. You dive deep into experiences."},
    30: {"name": "Feelings", "theme": "Clinging Fire", "description": "The gate of recognition of feelings. You feel deeply and desire experience."},
    31: {"name": "Influence", "theme": "Influence", "description": "The gate of influence and leadership. You lead through elected influence."},
    32: {"name": "Continuity", "theme": "Duration", "description": "The gate of continuity. You sense what will endure and what won't."},
    33: {"name": "Privacy", "theme": "Retreat", "description": "The gate of retreat and privacy. You process experiences through withdrawal."},
    34: {"name": "Power", "theme": "Great Power", "description": "The gate of power. You have pure sacral power and response."},
    35: {"name": "Change", "theme": "Progress", "description": "The gate of change and progress. You seek experiences and adventure."},
    36: {"name": "Crisis", "theme": "Darkening of the Light", "description": "The gate of crisis. You navigate emotional crises toward experience."},
    37: {"name": "Friendship", "theme": "The Family", "description": "The gate of friendship and bargains. You create community through loyalty."},
    38: {"name": "Fighter", "theme": "Opposition", "description": "The gate of the fighter. You fight for what has individual purpose."},
    39: {"name": "Provocation", "theme": "Obstruction", "description": "The gate of provocation. You provoke spirit and emotion in others."},
    40: {"name": "Aloneness", "theme": "Deliverance", "description": "The gate of aloneness. You need space and will to support community."},
    41: {"name": "Decrease", "theme": "Decrease", "description": "The gate of contraction. You feel the pressure of new emotional beginnings."},
    42: {"name": "Growth", "theme": "Increase", "description": "The gate of growth and finishing. You bring cycles to completion."},
    43: {"name": "Insight", "theme": "Breakthrough", "description": "The gate of insight. You have breakthrough knowing and unique perspectives."},
    44: {"name": "Energy", "theme": "Coming to Meet", "description": "The gate of energy and alertness. You remember patterns and transmit lessons."},
    45: {"name": "Gatherer", "theme": "Gathering Together", "description": "The gate of the gatherer and king. You gather resources and lead."},
    46: {"name": "Love of Body", "theme": "Pushing Upward", "description": "The gate of determination of self. You are in love with being in a body."},
    47: {"name": "Realization", "theme": "Oppression", "description": "The gate of realization. You make sense of abstract information."},
    48: {"name": "Depth", "theme": "The Well", "description": "The gate of depth. You have deep potential for taste and wisdom."},
    49: {"name": "Principles", "theme": "Revolution", "description": "The gate of revolution and principles. You accept or reject based on principles."},
    50: {"name": "Values", "theme": "The Cauldron", "description": "The gate of values and responsibility. You establish values and laws."},
    51: {"name": "Shock", "theme": "The Arousing", "description": "The gate of shock. You shock others into awakening and initiation."},
    52: {"name": "Stillness", "theme": "Keeping Still", "description": "The gate of stillness and inaction. You bring focus through stillness."},
    53: {"name": "Beginnings", "theme": "Development", "description": "The gate of beginnings and starting. You initiate new cycles of experience."},
    54: {"name": "Ambition", "theme": "The Marrying Maiden", "description": "The gate of ambition and drive. You are driven to rise and transform."},
    55: {"name": "Spirit", "theme": "Abundance", "description": "The gate of spirit and abundance. You carry emotional spirit and mood."},
    56: {"name": "Stimulation", "theme": "The Wanderer", "description": "The gate of stimulation. You stimulate others through ideas and stories."},
    57: {"name": "Intuition", "theme": "The Gentle", "description": "The gate of intuitive clarity. You have penetrating intuitive awareness."},
    58: {"name": "Vitality", "theme": "The Joyous", "description": "The gate of vitality and correction. You bring joy and aliveness through correction."},
    59: {"name": "Sexuality", "theme": "Dispersion", "description": "The gate of sexuality and intimacy. You break down barriers for connection."},
    60: {"name": "Acceptance", "theme": "Limitation", "description": "The gate of acceptance and limitation. You accept what is while mutating."},
    61: {"name": "Mystery", "theme": "Inner Truth", "description": "The gate of mystery and inner truth. You are inspired by life's mysteries."},
    62: {"name": "Details", "theme": "Preponderance of the Small", "description": "The gate of details. You express and organize precise details."},
    63: {"name": "Doubt", "theme": "After Completion", "description": "The gate of doubt and questioning. You question and seek logical proof."},
    64: {"name": "Confusion", "theme": "Before Completion", "description": "The gate of confusion. You make sense of the past through mental imagery."}
}

def get_gate_insights(gate_num):
    return GATE_INSIGHTS.get(gate_num, {
        "name": f"Gate {gate_num}",
        "theme": "Unknown",
        "description": f"This is Gate {gate_num}. Each gate carries unique energy and potential."
    })


# ==================== NOT-SELF GUIDANCE ====================

NOT_SELF_GUIDANCE = {
    "Generator": {
        "signs": [
            "Feeling frustrated with your work or life",
            "Initiating instead of waiting to respond",
            "Saying yes when your gut says no",
            "Exhausted but can't stop working",
            "Feeling stuck in the wrong job or relationship"
        ],
        "return_to_self": [
            "Stop and wait for something to respond to",
            "Practice checking your gut response on small decisions",
            "Quit commitments that consistently drain you",
            "Find work that lights you up",
            "Honor your body's no, even when your mind says yes"
        ]
    },
    "Manifesting Generator": {
        "signs": [
            "Frustration and anger simultaneously",
            "Scattered energy without responding first",
            "Starting too many things without completion",
            "Impatience with your own process",
            "Not informing others and facing resistance"
        ],
        "return_to_self": [
            "Wait for your Sacral response before jumping in",
            "Inform the people who will be impacted",
            "Trust your non-linear path - it's correct for you",
            "Allow yourself to skip steps and be efficient",
            "It's okay to pivot - just respond to the new direction"
        ]
    },
    "Manifestor": {
        "signs": [
            "Anger at being controlled or slowed down",
            "Constant resistance from others",
            "Feeling isolated or misunderstood",
            "Exhaustion from trying to have sustainable energy",
            "Acting without informing and facing consequences"
        ],
        "return_to_self": [
            "Inform before you act - not asking permission, just sharing",
            "Rest when you need to - you're not a Generator",
            "Find people who appreciate your power",
            "Initiate what's truly important to you",
            "Accept that your aura creates impact - use it wisely"
        ]
    },
    "Projector": {
        "signs": [
            "Bitterness about not being seen or recognized",
            "Exhaustion from trying to keep up with Generators",
            "Giving guidance that isn't invited or wanted",
            "Over-working to prove your worth",
            "Feeling like no one understands your value"
        ],
        "return_to_self": [
            "Wait for genuine invitations for the big things",
            "Rest much more than you think you need",
            "Study what fascinates you - mastery attracts invitations",
            "Focus on being recognized for who you are, not what you do",
            "Your value is inherent, not earned through work"
        ]
    },
    "Reflector": {
        "signs": [
            "Disappointment in people and places",
            "Feeling invisible or like you don't matter",
            "Making quick decisions you later regret",
            "Confusion about who you really are",
            "Being in unhealthy environments that drain you"
        ],
        "return_to_self": [
            "Wait a lunar cycle for major decisions",
            "Prioritize your environment above all else",
            "Journal to track your experience through the lunar cycle",
            "Find communities that feel healthy to reflect",
            "Embrace your uniqueness - you're literally rare"
        ]
    }
}

def get_not_self_guidance(hd_type):
    return NOT_SELF_GUIDANCE.get(hd_type, NOT_SELF_GUIDANCE["Generator"])


# ==================== DAILY PRACTICE ====================

def get_daily_practice(hd_type, authority):
    practices = {
        "Generator": {
            "morning": "Before starting your day, ask yourself: 'What am I excited to respond to today?' Notice your Sacral sounds and feelings. Don't force yourself into action - wait for something to spark your energy.",
            "evening": "Reflect: 'Did I honor my responses today? When did I feel satisfaction? When did I feel frustration? Did I commit to things my gut said no to?'",
            "weekly_experiment": "Practice saying 'let me check in with my gut' before committing to anything. Notice how different it feels when you respond correctly vs. when you initiate or override your gut.",
            "monthly_focus": "Identify one area of your life where you're not feeling satisfaction. Are you responding or initiating in that area? What would change if you only committed when your Sacral lit up?"
        },
        "Manifesting Generator": {
            "morning": "Check in with your body: 'What is pulling me today?' Trust your response, but before you leap, identify who you need to inform. Remember that your path may not be linear - and that's perfect.",
            "evening": "Reflect: 'Did I inform before acting? Did I trust my non-linear process? When did I feel frustrated? When did I skip steps correctly vs. miss something important?'",
            "weekly_experiment": "Practice informing someone before every major action you take. Notice how the resistance decreases and how much smoother things flow.",
            "monthly_focus": "Look at all your projects. Which ones light up your Sacral? It's okay to release what's no longer a 'yes' - your design is to be multi-passionate, not to finish everything you start."
        },
        "Manifestor": {
            "morning": "Set your intentions: 'What am I going to initiate today?' Remember to inform those who will be impacted. Plan for rest - your energy comes in bursts.",
            "evening": "Reflect: 'Did I inform others? Did I encounter unnecessary resistance? Did I honor my need for rest? Where did I feel peace vs. anger?'",
            "weekly_experiment": "Before each major action, send a simple text or message: 'Just wanted to let you know I'm going to...' Notice how differently people respond when they're informed.",
            "monthly_focus": "Identify where you're not feeling peace. Are you trying to work like a Generator? Are you not informing? Adjust your approach to honor your Manifestor nature."
        },
        "Projector": {
            "morning": "Set your intention: 'I am open to being recognized and invited today.' Focus on what you're studying or mastering. Don't push - let the invitations come.",
            "evening": "Reflect: 'Was I recognized today? Did I receive any invitations? Did I offer guidance that wasn't asked for? How much did I rest?'",
            "weekly_experiment": "Practice waiting to be asked before offering advice, even in casual conversations. Notice how much more your guidance is appreciated when it's invited.",
            "monthly_focus": "Are you feeling bitter about anything? That's your indicator you may be pushing rather than waiting. What area of your life needs more patience and trust?"
        },
        "Reflector": {
            "morning": "Notice: 'What am I feeling right now? How is my environment?' Remember that what you're feeling may not be yours. Check in with your physical surroundings.",
            "evening": "Journal: 'What did I sample today? Which energies felt good? Which felt off? How did my perspective shift?' Track these through the lunar cycle.",
            "weekly_experiment": "Pay close attention to how different environments affect you. Notice which spaces give you energy and which drain you. Your environment IS your strategy.",
            "monthly_focus": "Review your lunar month journal. What patterns do you notice? Any major decisions should be held until you've experienced the full cycle at least once."
        }
    }
    
    base_practice = practices.get(hd_type, practices["Generator"])
    
    # Add authority-specific guidance
    if authority == "Emotional":
        base_practice["morning"] += " Remember: there's no truth in the now. Notice where you are in your emotional wave."
        base_practice["evening"] += " Track your emotional wave. What decisions are you still processing?"
    
    return base_practice


# ==================== TRANSIT-BASED INSIGHTS ====================

def get_transit_morning_practice(hd_type, sun_gate, activating_gates):
    """Generate morning practice based on type and today's transits."""
    gate_info = GATE_INSIGHTS.get(sun_gate, {"name": "Unknown", "theme": "unknown"})
    
    type_intros = {
        "Generator": f"As a Generator, today's Sun in Gate {sun_gate} ({gate_info['name']}) invites you to notice what sparks your Sacral response.",
        "Manifesting Generator": f"MG energy today with Sun in Gate {sun_gate} ({gate_info['name']}) - stay alert for multiple things lighting you up. Remember to respond first, then inform.",
        "Projector": f"Today's Sun in Gate {sun_gate} ({gate_info['name']}) may bring invitations related to {gate_info['theme'].lower()}. Wait for recognition before sharing your insights.",
        "Manifestor": f"Gate {sun_gate} ({gate_info['name']}) energy today supports initiation around {gate_info['theme'].lower()}. Inform those who will be impacted.",
        "Reflector": f"Sample today's Gate {sun_gate} energy ({gate_info['name']}) and notice how it feels in different environments."
    }
    
    practice = type_intros.get(hd_type, type_intros["Generator"])
    
    if activating_gates:
        practice += f" Your gates {', '.join(map(str, list(activating_gates)[:3]))} are being activated - these themes are amplified for you today."
    
    return practice


def get_transit_focus(hd_type, authority, sun_gate):
    """Generate daily focus based on type, authority, and sun transit."""
    gate_info = GATE_INSIGHTS.get(sun_gate, {"name": "Unknown", "theme": "unknown"})
    
    authority_focus = {
        "Emotional": f"With {gate_info['theme']} themes present, wait for emotional clarity before any decisions. Notice how your wave moves today.",
        "Sacral": f"Let your gut guide you through Gate {sun_gate} themes. Listen for the 'uh-huh' or 'uhn-uhn' in situations involving {gate_info['theme'].lower()}.",
        "Splenic": f"Your intuition may speak about {gate_info['theme'].lower()} today. Trust those instant hits - they won't repeat.",
        "Ego": f"Ask yourself if your heart is truly in anything related to {gate_info['theme'].lower()} before committing.",
        "Self-Projected": f"Talk through any {gate_info['theme'].lower()} matters with trusted allies. Your truth will emerge through speaking.",
        "Mental": f"Notice your environment's health today. {gate_info['theme']} themes work best in the right setting.",
        "Lunar": f"You're sampling Gate {sun_gate}'s energy today. Notice how {gate_info['theme'].lower()} feels without committing to anything major."
    }
    
    return authority_focus.get(authority, authority_focus["Sacral"])


def get_transit_warning(hd_type, new_gates, not_self_info):
    """Generate warning based on type and transiting gates not in natal chart."""
    base_warning = not_self_info['signs'][0] if not_self_info['signs'] else "Going against your design"
    
    type_warnings = {
        "Generator": f"Watch for: {base_warning}. With gates {', '.join(map(str, list(new_gates)[:3]))} transiting (not in your chart), you may feel pulled to initiate rather than respond.",
        "Manifesting Generator": f"Watch for: {base_warning}. The transiting gates may tempt you to skip your Sacral response. Respond first, then move fast.",
        "Projector": f"Watch for: {base_warning}. Transiting gates may create pressure to prove yourself. Wait for genuine recognition.",
        "Manifestor": f"Watch for: {base_warning}. The collective transit energy isn't yours to carry. Initiate what's truly yours and rest.",
        "Reflector": f"Watch for: {base_warning}. Today's transits aren't your fixed energy - don't mistake sampled energy for who you are."
    }
    
    return type_warnings.get(hd_type, type_warnings["Generator"])


def get_transit_evening_question(hd_type, authority, activating_gates):
    """Generate evening reflection question based on type, authority, and activated gates."""
    
    type_questions = {
        "Generator": "Did I feel satisfaction today? When did my Sacral light up vs. when did I override it?",
        "Manifesting Generator": "Did I respond before acting? Did I inform? When did frustration arise?",
        "Projector": "Was I recognized today? Did I wait for invitations? Where did I feel bitterness?",
        "Manifestor": "Did I inform before acting? Where did I encounter resistance vs. flow?",
        "Reflector": "What did I sample today? Which environments felt healthy? What surprised me?"
    }
    
    base_q = type_questions.get(hd_type, type_questions["Generator"])
    
    if activating_gates:
        gates_str = ', '.join(map(str, list(activating_gates)[:2]))
        base_q += f" How did Gates {gates_str} show up in my experience?"
    
    return base_q


def get_transit_channel_insights(natal_gates, transit_gates):
    """Check if transits complete any channels with natal gates."""
    from hd_bodygraph import CHANNELS
    
    potential_channels = []
    
    for channel_key, channel_data in CHANNELS.items():
        gate1, gate2 = channel_data['gates']
        
        # Check if natal has one gate and transit has the other
        if gate1 in natal_gates and gate2 in transit_gates:
            potential_channels.append({
                'channel': channel_key,
                'name': channel_data['name'],
                'natal_gate': gate1,
                'transit_gate': gate2
            })
        elif gate2 in natal_gates and gate1 in transit_gates:
            potential_channels.append({
                'channel': channel_key,
                'name': channel_data['name'],
                'natal_gate': gate2,
                'transit_gate': gate1
            })
    
    return potential_channels
