const screenButton = document.getElementById("screenButton");

screenButton.addEventListener("click", async function () {

    const jobId = document.getElementById("jobId").value;
    const resumeInput = document.getElementById("resume");
    const message = document.getElementById("message");
    const resultBox = document.getElementById("result");

    if (jobId === "") {
        message.textContent = "Please enter a Job ID.";
        return;
    }

    if (resumeInput.files.length === 0) {
        message.textContent = "Please select a PDF resume.";
        return;
    }

    const file = resumeInput.files[0];

    const formData = new FormData();
    formData.append("file", file);

    message.textContent = "Screening candidate...";
    resultBox.classList.add("hidden");
    screenButton.disabled = true;

    try {

        const response = await fetch(
            `https://ai-recruitment-system-xruu.onrender.com/ai-screen-candidate/${jobId}`,
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        if (!response.ok) {
            message.textContent = data.detail || "Screening failed.";
            return;
        }

        document.getElementById("score").textContent =
            data.suitability_score + "%";

        document.getElementById("jobTitle").textContent =
            data.job_title;

        document.getElementById("candidateSkills").textContent =
            data.candidate_skills.join(", ");

        document.getElementById("matchedSkills").textContent =
            data.matched_skills.join(", ");

        document.getElementById("missingSkills").textContent =
            data.missing_skills.length > 0
                ? data.missing_skills.join(", ")
                : "None";

        document.getElementById("experience").textContent =
            data.candidate_experience +
            " years (Required: " +
            data.required_experience +
            " years)";

        document.getElementById("evidence").textContent =
            data.retrieved_evidence;

        document.getElementById("aiExplanation").textContent =
            data.ai_explanation;

        document.getElementById("cacheStatus").textContent =
            data.cache_status;

        resultBox.classList.remove("hidden");

        message.textContent = "Screening completed successfully.";

    } catch (error) {

        message.textContent =
            "Unable to connect to the FastAPI server.";

    } finally {

        screenButton.disabled = false;
    }
});