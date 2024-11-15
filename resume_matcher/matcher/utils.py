def cal_match_p(res_c, job_desc_c):
    res_w = set(res_c.lower().split())
    job_desc = set(job_desc_c.lower().split())
    # Calculate matching words
    matching_words = res_w.intersection(job_desc)
    total_words = len(job_desc)
    
    if total_words == 0:
        return 0.0
    
    match_p = (len(matching_words) / total_words) * 100
    return round(match_p, 2)