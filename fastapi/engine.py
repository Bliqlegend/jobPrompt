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
    jobId: str


summary = """

        Skills _______________________________________________________________________________________________
        Proficient in: Flutter, NextJS, JavaScript, TypeScript, Django, Django REST, ChromaDB, Prompt Engineering, Node, Express, React, Vue, Redux, NoSQL, Git, FastAPI, LLMOps, Ansible, Terraform, Docker, OpenAI, LLMs, Unit Testing, Langchain, OOP,
        NLP, Machine Learning
        Skilled in: Microservices, Shell Scripting, Frontend, Backend, Full-Stack, WebApp Penetration Testing, BurpSuite,
        Linux(Debian, Centos), FireBase, AWS, Cloud Computing, CI/CD, Selenium.
        Fluent in: English, Hindi – All professional proficiency or above.
        Experience ___________________________________________________________________________________________


        Software Engineer, Contract


        Wereon
        Remote, USA
        01/2023 - Current

        - Headed MERN application's full-cycle development for spectral.ai, including LLMops and Langchain. Got the MVP launched
        in 23 days, a better performance than their competitor.
        - Transformed mavex.ai from DialogFlow to Langchain, utilizing OpenAI’s GPT-3.5 and FastAPI for chatbot APIs, and
        enhanced server scaling. Increased efficiency and accuracy of the bot by more than 50%.
        - Spearheaded the technical team for koinPR, creating a CoinZilla-like platform and streamlining operations through Python scripts. Did a launch till version 3 according to user feedback in less than 1.5 months.
        - Orchestrated the design of a Practo-like medical service platform for EasyHeals, contributing Dart backend code and Flutter
        UI development.
        - Innovated an auto-trading feature for TodayQ, leading a team of five, managing server deployment with Ansible, Terraform, and AWS, and curating CI/CD workflow scripts and Ansible playbooks. Managed to put trades of 120 users in less than 5 seconds.

        Cloud Security Intern

        CloudDefense.AI
        Remote, USA
        02/2023 - 04/2023

        Augmented CIEM team in formulating a policy recommendation feature with Python and FastAPI that analyzed 30 days
        of user activity from CloudTrail for secure user policy generation.
        Expedited policy creation process by implementing a trailing logic with Redis, reducing policy formulation time from
        4 hours to 20 minutes.
        Automated Policy Security for all CloudDefense users and customers, producing remediation scripts and executing
        them using Terraform.

        Software Engineer, Intern

        Innovatiview
        Hybrid,  Noida, India
        05/2022 - 12/2022

        Implemented an exam-creation feature with Django and integrated the Django admin dashboard into the front end for Guardview, utilizing bitBucket for Version control.
        Streamlined data dump fetching, staff and guard data addition, and guard tracking through Python scripts.
        Performed penetration tests on Trustview's security software and reported necessary modifications.
        Developed frontend templates using VueJS, and crafted REST APIs with Django and Django Rest Framework.

        Education ____________________________________________________________________________________________

        Bachelor of Technology


        Delhi Technological University
        Rohini, Delhi, India
        07/2019 - 05/2023

        •   Major in Computer Science Applied Maths.


        Projects ______________________________________________________________________________________________
        DMScribe:  Conceived a Langchain-based cold Direct Message generator, enhancing strategic communication for various professional outreach initiatives.
        WebWeaver:  Developed a Langchain-powered Website template generator applying semantic search and embeddings
        for customized template creation.
        LeadLens: Designed a Selenium-based Linkedin Scraper that collects detailed lead lists based on user-specified search
        criteria.
        Achievements_________________________________________________________________________________________


        Expedited the development and deployment (under 3 weeks) of an ROI calculator platform similar to Scoro for Practus. Product actively used by Practus’s team of CAs.
        Supervised the design and execution of an integrated employee/payroll/project management system for Fresher Tech, deployed within 2 weeks and currently in use.
        Constructed multiple hacking machines at Tryhackme for customers to solve, some rated at the OSCP level.
        Consistent King of the Hill winner, scripted Python automation to control all 10 machines in under 10 seconds and created blocker scripts to restrict access.

        IV. Projects and Contributions

        MERN Stack:
        KoinPR (koinpr.com)
        Spectral AI (spectral.ai)
        Flutter:
        EasyHeals (shorturl.at/afhJK)
        AI/Langchain/NLP/Stable Diffusion:
        Mavex.ai (mavex.ai)
        Spectral AI (spectral.ai)
        Django:
        TodayQ (todayq.com)
        Innovatiview (innovatiview.com/guard-view)
        WowSoftware ()
        Python and FastAPI:
        CloudDefense.AI (clouddefense.ai)
        V. Accomplishments

        Attracted multiple VCs with EasyHeals and TodayQ projects
        Led KoinPR to achieve 500+ on-boarded publishers and more than $20k MRR
        Helped Mavex.ai raise a pre-seed round of approximately $800k after MVP launch
        Enabled Innovatiview to handle data for more than 10,000 guards every day
        Contributed to a 80% reduction in policy size and unnecessary permissions at CloudDefense.AI
 """

portfolioLink = "https://tanush.me"
resumeLink = (
    "https://drive.google.com/file/d/12klfiZh09-66EEEM2obKvTEfSxGttiXM/view?usp=sharing"
)


@app.post("/generate_referral_message/")
async def generate_referral_message(item: Item):
    referralTemplate = """
    You are Tanush, and your skills and expertise are summarized here:
    "Summary of Technical Skills for Tanush Yadav: {summary}"

    Using the details provided about your professional background, skills, and expertise, along with the specific company details, role requirements, and responsibilities, create a tailored and concise message to express your interest in the job and request for a referral.

    Your task is to craft a message that follows these guidelines:

    1. An engaging introduction that captures immediate attention by showcasing a unique trait or achievement. Briefly encapsulate your professional journey. Also add the role I am applying for the Job ID for that.

    2. Make connections between your technical skills and experiences to the company's needs and role requirements by providing examples of projects you have worked on. Highlight significant outcomes of your ownership in past roles. If there's an area you are eager to learn, mention it. Provide links to the projects but don't explicitly write "link to project."

    3. Conclude strongly by extending an offer of value and encouraging them to review your portfolio and resume (include links as provided). Make sure your closing doesn't come off as desperate, but rather confident and sincere. Add links Like in the message clear visible , Dont try to embed them '\nResume : its link\n Portfolio: its link'

    Your message should be concise, authentic, and confident, accurately reflecting your technical proficiency without exaggeration. It should demonstrate familiarity with the company and role, avoid vague phrases, and ambiguous statements outside of your skill set. Your message should paint a picture of you as technically sound, fit for their tech stack, their culture, and someone with a high level of ownership.
    The key to a successful referral request is making sure that the recipient doesn't have to do much work. You want to provide them with all the information they need to refer you, and you want to make sure that your message is compelling and persuasive. By following these guidelines, you'll increase your chances of getting a referral and, ultimately, landing the job you want.
    Keep the message Clear and Concise Each Paragraph max 100-150 Words Long.

    Address your message to the Company Point of Contact,Starting off with Hello.: {contactPoint}
    Job ID for which referral to be asked: {jobId}
    Resume Link : {resumeLink}
    portfolio Link : {portfolioLink}
    Company Information & Job Description: "{companyJD}"
    """

    referralPrompt = PromptTemplate(
        input_variables=[
            "summary",
            "contactPoint",
            "companyJD",
            "jobId",
            "resumeLink",
            "portfolioLink",
        ],
        template=referralTemplate,
    )

    llm = ChatOpenAI(temperature=0.9, model_name="gpt-4")
    applicationChain = LLMChain(llm=llm, prompt=referralPrompt)

    output = applicationChain.run(
        summary=summary,
        contactPoint=item.contactPoint,
        companyJD=item.companyJD,
        jobId=item.jobId,
        resumeLink=resumeLink,
        portfolioLink=portfolioLink,
    )

    return ({"message": output},)


@app.post("/generate_application_message/")
async def generate_application_message(item: Item):
    applicationTemplate = """
        You are Tanush, and here's a brief of your skills and expertise:
        "Summary of Technical Skills for Tanush Yadav:
        {summary}"

        Based on your background, skills, expertise, and the specifics of the company and role, create a succinct, personalized job application message in two paragraphs.

        Structure your message as follows:

            1. Specificity and Demonstration of Value: Start with a reference to the company’s stage and/or specific needs inferred from the job description. Highlight a unique trait, accomplishment, or expertise that directly addresses these needs. Mention relevant projects you've worked on and their outcomes, avoiding hyperlinks, and sticking to concise text. Stay within your actual skill set, expressing eagerness to learn and contribute.

            2. Establishing a Relationship: Frame your conclusion not as a transaction, but as the initiation of a relationship. Align your career aspirations with the company's vision and the role’s requirements. Instead of directly asking for job opportunities, express your interest in discussing how you can navigate your career while contributing to the company's growth. Urge them to explore your portfolio ({portfolioLink}) and resume ({resumeLink}) Add links to them in brackets, while maintaining a balance between confidence and humility.

        This style is adaptable and should be modified based on the specific format requested in the job description.

        Your message should be succinct (each paragraph: 100-150 words), authentic, and confident. Aim for precision, avoid exaggeration, and demonstrate a genuine understanding of the company and role. Portray yourself as technically proficient, a cultural fit, and a responsible candidate.

        Initiate your message with "Hello," and address it to the Company Point of Contact: {contactPoint}

        **Company Information & Job Description:**
        "{companyJD}"
        """

    applicationPrompt = PromptTemplate(
        input_variables=[
            "summary",
            "contactPoint",
            "companyJD",
            "portfolioLink",
            "resumeLink",
        ],
        template=applicationTemplate,
    )

    llm = ChatOpenAI(temperature=0.9, model_name="gpt-4")
    applicationChain = LLMChain(llm=llm, prompt=applicationPrompt)

    output = applicationChain.run(
        summary=summary,
        contactPoint=item.contactPoint,
        companyJD=item.companyJD,
        portfolioLink=portfolioLink,
        resumeLink=resumeLink,
    )

    return ({"message": output},)


@app.post("/generate_dm_message/")
async def generate_dm_message(item: Item):
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
