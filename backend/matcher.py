def match_skills(candidate_skills, job_skills):

    matched_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill in candidate_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills

def match_experience(candidate_experience, required_experience):

    if candidate_experience >= required_experience:
        return True
    else:
        return False

def calculate_score(matched_skills, job_skills, experience_match):

    if len(job_skills) == 0:
        skill_score = 0
    else:
        skill_score = (len(matched_skills) / len(job_skills)) * 80

    if experience_match:
        experience_score = 20
    else:
        experience_score = 0

    total_score = skill_score + experience_score

    return round(total_score, 2)

def rank_candidates(candidates):

    ranked_candidates = sorted(
        candidates,
        key=lambda candidate: candidate["suitability_score"],
        reverse=True
    )

    return ranked_candidates

