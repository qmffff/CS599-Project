from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key='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')
# speech_file_path = Path(__file__).parent / "conference_intro_moderator.mp3"
# response = client.audio.speech.create(
#   model="tts-1",
#   voice="alloy",
#   input=("Ladies and gentlemen, welcome to our conference on 'The Future of Artificial Intelligence.' "
#          "I am delighted to host today's discussion with a distinguished panel of experts, each with a unique "
#          "perspective on where AI is heading. We're looking to explore some of the most pressing questions and "
#          "themes that are likely to shape this rapidly evolving field. "
#          "For round 1 of our discussion, I’m pleased to introduce our speakers: "
#          "1. Dr. Susan Clarke, a leading expert in machine learning and neural networks with over 15 years of research experience at top-tier universities. "
#          "2. Professor Amir Khan, an authority in robotics and automation, distinguished for his contributions to ethical AI design and policy advocacy. "
#          "3. Dr. Ravi Gupta, a prominent data scientist with a focus on AI applications in healthcare and the potential for personalized medicine. "
#          "4. Ms. Lisa Blackwood, a technology entrepreneur well-known for her innovative start-up that integrates AI with renewable energy systems. "
#          "5. Mr. Henry Tam, a renowned AI ethicist who has led numerous panels on the implications of AI in society and human rights. "
#          "6. Engineer Maya D'Souza, with a strong background in AI implementation in smart city infrastructure and sustainable urban development. "
#          "7. Ms. Sandra Chen, a venture capitalist specializing in AI startups, particularly looking at scalability and market disruption. "
#          "Our order of speaking will be as follows: [Dr. Susan Clarke, Professor Amir Khan, Dr. Ravi Gupta, Ms. Lisa Blackwood, Mr. Henry Tam, Engineer Maya D'Souza, Ms. Sandra Chen]. "
#          "I urge each speaker to share their insights and provocations while adhering to our time limits. As host, I reserve the right to regulate our discussion, including the addition or removal of speakers in subsequent rounds to best accomplish the tasks of our meeting. "
#          "Without further ado, let's delve into our discussion on the future of artificial intelligence. Dr. Susan Clarke, the floor is yours.")
# )
# response.stream_to_file(speech_file_path)

speech_file_path = Path(__file__).parent / "1dr_susan_clarke_speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="shimmer",
  input=("Thank you very much for the warm introduction. I am Dr. Susan Clarke, and I have dedicated the majority of my career to exploring the depths of machine learning and neural networks. It is an honor to be here among such esteemed colleagues. "
         "When we contemplate the future of artificial intelligence, I believe we should focus on three pivotal themes: advancement of AI algorithms, ethical considerations, and the accessibility of AI technology. "
         "Firstly, the development of AI algorithms is becoming increasingly complex and capable. With the recent advances in deep learning, we're now able to process data at an unprecedented scale. My research suggests that with the refinement of neural network architectures, such as the advent of Transformer models, we will likely see AI systems that can navigate more abstract and complex environments, enhance creativity, and improve decision-making. "
         "However, with great power comes great responsibility. Ethical considerations are at the forefront of AI development. Ensuring that AI systems are fair, transparent, and unbiased is not just a technical challenge but also a societal imperative. We need to establish clear guidelines and frameworks to govern AI and protect individuals' rights, especially as AI becomes more integrated into daily life. "
         "Accessibility, the third theme, is about ensuring that the benefits of AI are widely distributed throughout society. While large tech companies currently dominate AI advancements, I am an advocate for open-source projects and collaborations that enable small-scale researchers and developers to contribute and have access to high-level AI technology. "
         "In the future, I envision an AI that is not only powerful and ethical but also diverse and inclusive, contributing to advancements across all sectors of society. To achieve this vision, we as a community must commit to open dialogues, interdisciplinary collaborations, and the relentless pursuit of knowledge. "
         "I look forward to hearing the perspectives of my fellow panelists on these topics, and I am hopeful for what we can achieve collectively. Thank you. "
         "Now, I would like to pass the discussion over to Professor Amir Khan.")
)

response.stream_to_file(speech_file_path)

# speech_file_path = Path(__file__).parent / "2professor_khan_speech.mp3"
# response = client.audio.speech.create(
#   model="tts-1",
#   voice="echo",
#   input=("Thank you, Dr. Clarke, for your insightful remarks and to our moderator for facilitating this session. "
#          "I am Professor Amir Khan, with a background in robotics and a profound interest in the intersection of ethical AI design and policy. "
#          "Building upon the themes that Dr. Clarke highlighted, I want to emphasize the importance of anticipating the societal impact of AI and robotics as we advance. "
#          "The robots of tomorrow, powered by AI, won't just be confined to industrial settings; they will walk our streets, manage our homes, and assist in our workplaces. "
#          "We are heading toward a future where human-robot interaction becomes commonplace, and ensuring that this coexistence is harmonious is paramount. "
#          "We face a dual challenge: how to design robots that are capable of understanding and operating within human social norms while also ensuring that our policies keep pace with the technological advancements to safeguard public interest. "
#          "Ethical AI design is not merely about creating algorithms that are fair and unbiased; it extends to crafting robots that respect privacy, dignity, and autonomy. "
#          "As an advocate for responsible AI, my work focuses on embedding ethical principles in the design phase of robotics. "
#          "Transparency in how robots make decisions, designing for privacy, and the ability to work alongside humans without displacement are all critical areas that need our attention. "
#          "Additionally, policies must evolve as swiftly as the robots themselves. Government, industry, and academia need to form robust partnerships to craft regulations that are flexible enough to foster innovation but stringent enough to prevent misuse. "
#          "The transformation AI and robotics will bring to our workforce also requires that we reskill and prepare the current and future generations for a vastly different job market. "
#          "We stand at the precipice of a new era, ripe with potential yet fraught with challenges. By holding the reigns tightly on the ethical and societal implications of AI, we have the power to steer technology towards a future that benefits humanity as a whole. "
#          "I thank you all for your attention and look forward to the contributions from the rest of our esteemed panel. Now, I pass the baton to Dr. Ravi Gupta, a visionary in the application of AI in healthcare. Dr. Gupta, please share your perspectives with us.")
# )

# response.stream_to_file(speech_file_path)
