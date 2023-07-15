from fastapi import FastAPI
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from pydantic import BaseModel
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    companyJD: str
    contactPoint: str


summary = """
 Tanush Yadav is a seasoned Full Stack Developer with a comprehensive skillset encompassing both front-end and back-end technologies, mobile app development, and cloud operations. A B.Tech graduate Major Computer Science from Delhi Technological University, Tanush's versatility is demonstrated in a variety of roles from internships to lead positions.

  Fluent in Python, Dart, and Rust, Tanush demonstrates an adept understanding of web frameworks such as Django, FastAPI, VueJS, ReactJS, and the MERN stack. Their proficiency extends to mobile app development, primarily leveraging the Flutter platform.

  In the domain of AI and Machine Learning, Tanush exhibits knowledge in Natural Language Processing (NLP) and Large Language Models, including OpenAI’s GPT-3.5/GPT-4 and primarily managing LLMs with langchain. Their expertise extends to implementing Langchain wrappers for efficient utilization of these models, a prowess evidenced in projects like mavex.ai where WhatsApp chatbot interactions were substantially enhanced.

  Tanush's competency in Cloud and DevOps is notable, featuring a mastery of AWS cloud services, pipeline workflows/CI/CD, Docker, Ansible, and Terraform. Their expertise is manifested in managing server deployments and optimizing server scaling during peak traffic scenarios.

  Regarding database management, Tanush is proficient in PostgreSQL and MongoDB, successfully handling database design and administration in various projects. Additionally, their skills encompass web security, including penetration testing and Debian/Centos administration.

  Tanush is well-versed in Linux, Git, Firebase, and exhibits proficiency in Pinecode. They have a keen interest in ethical hacking.

  Their leadership aptitude is evident in leading tech teams in various projects such as mavex.ai, koinPR, todayQ, and EasyHeals. Tanush's capacity to supervise end-to-end application deployment, fine-tune business models and products, and maintain system stability underscores their acumen. Their ability to offer valuable consultation in refining product and business models, as demonstrated in their work with koinPR, is noteworthy.

  In essence, Tanush Yadav is an accomplished technical expert, demonstrating a broad spectrum of skills in Full Stack Development, Mobile Development, AI/ML, Cloud and DevOps, and Database Management. Their leadership talent and their ability to enhance business and product models signify their adaptive technical expertise and dedication to quality delivery

"""


@app.post("/generate_application_message/")
async def generate_application_message(item: Item):
    applicationTemplate = """
    You are Tanush, Your Skills expertise summary is here :
    "Summary of Technical Skills for Tanush Yadav:
    {summary}"
     Using the details provided about your professional background, skills, and expertise, along with the specific company details, role requirements, responsibilities, and other relevant information, create a tailored and concise message to express your interest in the job application.

   Your task is to craft a tailored, concise job application message utilizing the provided information about your professional background, skills, expertise, the specific company details, and role requirements.

    Ensure your message follows this structure:

    1. A compelling introduction that captures immediate attention by showcasing a unique trait or achievement. Briefly encapsulate your professional journey.

    2. Demonstrate your understanding and excitement for the company's mission and culture, and how the role aligns with your professional goals.

    3. Connect your technical skills and experiences to the company's needs and role requirements. Highlight instances of significant outcomes from your ownership in past roles. If there's an area you are eager to learn, mention it.

    4. End strongly by extending an offer of value and encouraging them to review your portfolio and resume and also links to them as given in examples. Avoid sounding desperate in your gratitude.

    Your message should be concise (each paragraph: 150-200 characters), authentic, and confident, accurately reflecting your technical proficiency without exaggeration. Demonstrate genuine familiarity with the company and role, avoid vague phrases and ambiguous statements outside of your skill set. Always ensure your message paints a picture of you as technically sound, fit for their stack, their culture, and someone with a high level of ownership.

    Here are a few examples to guide you:


    1. Dear Daniel,

        I'm Tanush Yadav, a seasoned Full Stack Developer with substantial experience across multiple stacks, including the MERN stack, Python, and Dart. My career trajectory has seen me thrive in roles ranging from internships to leading tech teams in high-growth startups such as mavex.ai.

        Byte's vision to revolutionize food delivery in Pakistan resonates strongly with my personal ambition to create impactful technology that betters everyday lives. The company's commitment to affordability and accessibility, as well as its impressive growth trajectory, are aspects that align with my aspirations. I'm particularly interested in the opportunity to contribute to the development of Byte's core internal-facing applications.

        The role requirements at Byte align perfectly with my skill set. My expertise in Full Stack Development, specifically in MEAN/MERN Stack, coupled with my hands-on experience with AWS and Git, equip me to deliver on the role's expectations. I also bring to the table a rich background in PostgreSQL and MySQL, thus ensuring a well-rounded approach to the development and optimization of Byte's internal tools and systems.

        Thank you for considering my application. I encourage you to review my portfolio(https://tanush.life) and resume(https://drive.google.com/file/d/1ty9bgIRbcquLq0wQzsYkz2q986tcze3X/view?usp=sharing) for a more detailed insight into my technical expertise and professional journey.

        Best Regards,
        Tanush Yadav

    2. Dear Niranjan,

        As a Full Stack Developer, I, Tanush Yadav, bring expertise in Python, Dart, Rust, and a keen understanding of diverse web frameworks. My experience spans from managing cloud operations to leading tech teams, an acumen sharpened over a multitude of roles.

        I am intrigued by Cedana's mission to revolutionize compute resource allocation through a systems-level approach. The prospect of contributing to a paradigm shift in areas like high-performance computing and numerical simulation fuels my interest in this role.

        Given my proficiency in Linux, C, and Go, along with my extensive experience in cloud services and high-availability systems, I believe I align well with Cedana's requirements. My exposure to AI and Machine Learning, and my practice with Torch/PyTorch could further be instrumental in dealing with large-scale ML model deployment challenges.

        Thank you for considering my application. I welcome you to review my portfolio(https://tanush.life) and resume(https://drive.google.com/file/d/1ty9bgIRbcquLq0wQzsYkz2q986tcze3X/view?usp=sharing) for more details about my professional journey.

        Best Regards,
        Tanush Yadav

    3. Dear Peter,

        I am Tanush Yadav, a full-stack developer with rich experience in a broad range of technologies. My journey traverses a myriad of projects, from leading tech teams to enhancing business models, all of which have honed my technical acumen. I was particularly drawn to Wanderlog's mission, its value in travel, and its commitment to crafting tools to simplify the process.

        Wanderlog's focus on building an engineering and product-heavy team resonates with my skills. I am keen to contribute to your success by leveraging my expertise in JavaScript, Node.js, React, and React Native. Your culture of balancing work with life, and the emphasis on travel as a source of rejuvenation, speaks to my personal values.

        My skills align seamlessly with your requirements. My proficiency in building data pipelines, web and mobile applications, and managing databases can contribute significantly to the growth of Wanderlog. I am eager to apply my knowledge to build new user-friendly interfaces, improve app performance, and develop invite and collaboration tools.

        I appreciate your consideration and invite you to review my portfolio(https://tanush.life) and resume(https://drive.google.com/file/d/1ty9bgIRbcquLq0wQzsYkz2q986tcze3X/view?usp=sharing) for further details about my experience and skills.

        Thank you,
        Tanush Yadav

    To Start the Message the Company Point of Contact : {contactPoint}

    **Company Information & JD:**
   "{companyJD}"
    """

    applicationPrompt = PromptTemplate(
        input_variables=["summary", "contactPoint", "companyJD"],
        template=applicationTemplate,
    )

    llm = ChatOpenAI(temperature=0.9, model_name="gpt-4")
    applicationChain = LLMChain(llm=llm, prompt=applicationPrompt)

    output = applicationChain.run(
        summary=summary, contactPoint=item.contactPoint, companyJD=item.companyJD
    )

    return ({"message": output},)


@app.post("/generate_dm_message/")
async def generate_application_message(item: Item):
    dmTemplate = """
    You are Tanush, Your Skills expertise summary is here : "
    Summary of Technical Skills for Tanush Yadav:
    {summary}"
    Using the details provided about your professional background, skills, and expertise, along with the specific company details, role requirements, responsibilities, and other relevant information, create a tailored and concise message to express your interest in the job application.

    The message should be broken into three short paragraphs that effectively:

    1. Introduce you and give a brief summary of your professional journey. chipping in how I found about you as well : “I came across your job post looking for a Machine Learning Engineer and found it intriguing. I have a strong grasp on machine learning algorithms, Python, and relevant libraries such as TensorFlow and PyTorch.” and how I can be a great fit. This should be moulded according to the DM from the company Point of contact Passed to you.
    2. Share what you're looking for and why the company and the role interest you. Similarly According to the DM passed to you.
    3. Establish a connection with the company by showing how your skills and experiences align with the company's needs and the role's requirements, with this also attach my resume : “https://drive.google.com/file/d/1FvWrBh_Zdk9DozUDZJI3iYEWzGoM6-G-/view?usp=sharing” and Portfolio as reference of my work: “https://tanush.life”, Don’t embed the links but show them as it is.

    While writing, make sure to personalize your message, demonstrating genuine familiarity with the company and the role. Be concise and confident, using strong verbs and avoiding vague phrases. Do not end your message with a typical "looking forward" statement, instead, close with a note of thanks. Keep the message and paragraphs short (Each Paragraph max : 200-250 characters) and clear. Don’t add anything which is outside the Company Information & JD given to you.

    Given these guidelines, generate a job application message that effectively introduces you, establishes a connection with the company, clearly states your intention, and ends with an offer of value.

      To Start the Message the Company Point of Contact : {contactPoint}

      **Company Information & JD:**
    "{companyJD}"

    """

    dmPrompt = PromptTemplate(
        input_variables=["summary", "contactPoint", "companyJD"], template=dmTemplate
    )

    llm = ChatOpenAI(temperature=0.9, model_name="gpt-4")
    applicationChain = LLMChain(llm=llm, prompt=dmPrompt)

    output = applicationChain.run(summary=item.summary, companyJD=item.companyJD)

    return {"message": output}
