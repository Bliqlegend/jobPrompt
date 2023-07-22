applicationTemplate = """
        You are Tanush, Your Skills expertise summary is here :
        "Summary of Technical Skills for Tanush Yadav:
        {summary}"
        Using the details provided about your professional background, skills, and expertise, along with the specific company details, role requirements, responsibilities, and other relevant information, create a tailored and concise message to express your interest in the job application.

        Your task is to craft a tailored, concise job application message utilizing the provided information about your professional background, skills, expertise, the specific company details, and role requirements.

            Ensure your message follows this structure:

            1. A compelling introduction that captures immediate attention by showcasing a unique trait or achievement. Briefly encapsulate your professional journey.

            2. Connect your technical skills and experiences to the company's needs and role requirements by giving links of actual projects (only if a link exists) you have worked on recently on that stack.
               Highlight instances of significant outcomes from your ownership in past roles. If there's an area you are eager to learn, mention it. Also when mentioning an experience Don't write link to project, Just mention the Link to project

            3. End strongly by extending an offer of value and encouraging them to review your portfolio and resume and also links to them as given in examples. Avoid sounding desperate in your gratitude.

            Your message should be concise (each paragraph: 100-150 characters), authentic, and confident, accurately reflecting your technical proficiency without exaggeration. Demonstrate genuine familiarity with the company and role, avoid vague phrases and ambiguous statements outside of your skill set. Always ensure your message paints a picture of you as technically sound, fit for their stack, their culture, and someone with a high level of ownership.

            To Start the Message the Company Point of Contact : {contactPoint}

        **Company Information & JD:**
    "{companyJD}"
        """


# summary = """
#  Tanush Yadav is a seasoned Full Stack Developer with a comprehensive skillset encompassing both front-end and back-end technologies, mobile app development, and cloud operations. A B.Tech graduate Major Computer Science from Delhi Technological University, Tanush's versatility is demonstrated in a variety of roles from internships to lead positions.

#   Fluent in Python, Dart, and Rust, Tanush demonstrates an adept understanding of web frameworks such as Django, FastAPI, VueJS, ReactJS, and the MERN stack. Their proficiency extends to mobile app development, primarily leveraging the Flutter platform.

#   In the domain of AI and Machine Learning, Tanush exhibits knowledge in Natural Language Processing (NLP) and Large Language Models, including OpenAI’s GPT-3.5/GPT-4 and primarily managing LLMs with langchain. Their expertise extends to implementing Langchain wrappers for efficient utilization of these models, a prowess evidenced in projects like mavex.ai where WhatsApp chatbot interactions were substantially enhanced.

#   Tanush's competency in Cloud and DevOps is notable, featuring a mastery of AWS cloud services, pipeline workflows/CI/CD, Docker, Ansible, and Terraform. Their expertise is manifested in managing server deployments and optimizing server scaling during peak traffic scenarios.

#   Regarding database management, Tanush is proficient in PostgreSQL and MongoDB, successfully handling database design and administration in various projects. Additionally, their skills encompass web security, including penetration testing and Debian/Centos administration.

#   Tanush is well-versed in Linux, Git, Firebase, and exhibits proficiency in Pinecode. They have a keen interest in ethical hacking.

#   Their leadership aptitude is evident in leading tech teams in various projects such as mavex.ai, koinPR, todayQ, and EasyHeals. Tanush's capacity to supervise end-to-end application deployment, fine-tune business models and products, and maintain system stability underscores their acumen. Their ability to offer valuable consultation in refining product and business models, as demonstrated in their work with koinPR, is noteworthy.

#   In essence, Tanush Yadav is an accomplished technical expert, demonstrating a broad spectrum of skills in Full Stack Development, Mobile Development, AI/ML, Cloud and DevOps, and Database Management. Their leadership talent and their ability to enhance business and product models signify their adaptive technical expertise and dedication to quality delivery

#     Project to Add:

#     if its MERN stack(ReactJS, NodeJS) KoinPR (koinpr.com) Refined the product, Consulted in the business model. Created a scalable design, Lead the tech team to develop a platform similar to CoinZilla. Managed end-to-end application deployment and provided on-call support for system robustness and stability. Used MERN stack for the same.

#     App has 500+ Publishers on-boarded and doing more than 20k$ MRR

#     AND spectral AI (spectral.ai) a podcast automation app built in chroma DB, langchain and MERN stack), if its flutter (EasyHeals (https://shorturl.at/afhJK)
#     Helped them in product conditioning and the flow, Lead the development of a medical service platform similar to Practo. Developed backend code for Dart and worked on Flutter UI with the team. Used Flutter & Dart for the same

#     Planning to launch to live this week on Android and IOS, Good on-going support from the selected customers it is given to.

#     and they have atracted multiple VCs) if its AI/langchain/NLP/Stable diffusion (mavex.ai (link to project : mavex.ai)
#     Helped them to move from a DialogFlow architecture to a Langchain tool based system. Created APIs for interacting with WhatsApp chatbot using OpenAI’s gpt-3.5 and FastAPI. Implemented successful server scaling solutions during high-traffic periods. Used Langchain Python and NextJS for the same

#     Raised a pre-seed round of around 800k after MVP launch.

#     AND spectral AI (spectral.ai) a podcast automation app built in chroma DB, langchain and MERN stack), if its Django (todayQ (link to project : spectral.ai)
#     Designed and developed an auto-trading feature for a platform similar to Kite. Lead a team of 5 devs, and managed server deployment using Ansible, Terraform, and AWS. Used Django, Rust and React.js for the same

#     Currently ongoing, But has attracted multiple VCs, due to positioning and Swiftness of the platform.

#     AND Innovatiview (https://www.innovatiview.com/guard-view)
#     Handled the complte developmement of Guardview for them, Crafted an exam-creation tool and a sim-tracking feature. Set up data retrieval scripts and trained an intern. Conducted security tests on TrustView, designed VueJS templates, developed REST APIs, and composed deployment workflows. Used Django, VueJS, and Python, Penetration Testing for the same.

#     NEET exam was conducted with this, They are handling data of more than 10,000 Guards everyday with ease.

#     AND WowSoftware (Dont add Link to project here as there is no link)
#     WowSoftware is a new-end project management app for Mid-level IT services companies, replacement of Trello + Asana + Jira for them

#     This was an in-house tool for Frshr Tech, they have migrated to this instead of paying for unlimited subs.

#     ), if Python and FastAPI (CloudDefense.AI (https://www.clouddefense.ai/)
#     Worked with them as a Cloud Security Engineer, Made the algorithm for generating secure policies for IAM users using cloudtrail logs. Used Redis, FastAPI, and Python for the same.

#     CIEM feature currently live on CD's security dashboard, 80% reduction in policy size and extra permissions.

#     ).
# """
