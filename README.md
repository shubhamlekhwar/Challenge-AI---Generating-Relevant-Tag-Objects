# skill_tagging

Project Context
    This challenge is a part of a brand new project to introduce new AI based capabilities to the Topcoder platform. As of now, the project's immediate goal is to extract useful information from the challenge specification and explore its use cases.
Challenge Context
    Within the project context mentioned above, the current challenge aims to deliver an implementation that can generate relevant tags for a challenge, using its challenge specification as input.

2. Expected Outcome

    A command-line or API based tool that takes challenge specification string as input and returns a list of tag objects that are relevant to the challenge specification.The exact nature of this expected list and the tag objects are described in the Expected output sub-section under the Challenge Details section below.

3. Challenge Details

    Dataset
    The dataset (in JSON format) can be found in the forum thread. The data is in the format:

    challenge_id: {
        "sub_track": sub_track of the challenge,
        "challenge_url": url of the challenge,
        "technologies": the list of technology tags of challenges,
        "platforms": list of platform tags of the challenge,
        "challenge_spec": the challenge specification string including HTML
    }
    Input
    It should be noted that although five attributes of the challenges have been provided, the final implementation should take a string, i.e. only challenge_spec value as input to generate the output. The other details can be used as needed to improve the program. Here, the input string can either be with or without the HTML. The tool should be able to handle both cases.
    Expected output format
    The output of the tool should be a list of string tags, or a list of tag objects, where each object can include additional metadata about the tag. For example, if the generated tags are: 'Python', 'Machine Learning', 'NLP', 'Shopping', 'e-commerce', 'Data Scientist', then the output should be a list of objects:

    [
        {
            tag: 'Python',
            type: 'required_skill',
            source: 'external_EMSI'},
        {
            tag: 'Machine Learning',
            type: 'required_skill' ,
            source: 'external_EMSI'},
        {
            tag: 'NLP',
            type: 'required_skill',
            source: 'external_EMSI'},
        {
            tag: 'Shopping',
            type: 'problem_domain',
            source: 'custom'},
        {
            tag: 'e-commerce',
            type: 'problem_domain',
            source: 'external_ABCD'},
        {
            tag: 'Improve Sales',
            type: 'summary_phrases',
            source: 'custom'}

    ]

    Hence, the expected attributes of each tag object are:
        tag - the name of the tag
        type - the category of the tag. Competitors are free to create a list of their categories. Some ideas of tag categories can be: 'required_skill', 'problem_domain', 'target_audience' 'summary_phrases' etc. Among these, 'required_skill', 'problem_domain' are essential, and any additional categories are optional but are welcome and can potentially lead to a higher review score.
        source - the source of this tag. If the value has been suggested by a custom model or implementation built by the competitor, it's source attribute should be set to 'custom'. If the tag has been extracted from an external API/service, like EMSI, then the tag object's source should be set to 'external_XYZ', where XYZ is the name of the service. For example, any tag that has been received from the EMSI service should have the source attribute as 'external_EMSI'. In fact, the use of EMSI is required for skill tags. (For more details about EMSI, kindly check the 'External Data' section below.
        match_score - (Optional) the estimated confidence score of how well the tag matches with the spec. Here the accuracy of this score is optional and hence not extremely important, and will not affect the review score unless it is particularly misleading.
        Any additional optional attribute which might be useful can be included.
    Important note about Technology and Platform Tags
    The platform and technologies tags are available for some of the challenges (mostly Development challenges) in the provided dataset. It should be noted that the tags might not be reliable as they are assigned manually by copilots and are at times not exhaustive.
    Furthermore, although it is expected that output for Code challenge spec inputs contain similar kinds of tags, the expected output tags should NOT be limited to just tags that are similar to current type of technology and platform tags. The output tags should ideally also contain additional kinds of tags, such as the 'problem_domain', 'summary_phrases' tags etc described above.
    External Data
    In addition to any custom NLP implmentations, any use of external data and resources is not only allowed but is encouraged.

    
