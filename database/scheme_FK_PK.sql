-- Set respondent_id as the primary key in the mental_health_survey table
ALTER TABLE mental_health_survey
ADD CONSTRAINT pk_respondent_id PRIMARY KEY (respondent_id);

-- Add foreign key constraint to the mental_health_conditions table
ALTER TABLE mental_health_conditions
ADD CONSTRAINT fk_mental_health_conditions_respondent_id
FOREIGN KEY (respondent_id)
REFERENCES mental_health_survey (respondent_id);

-- Add foreign key constraint to the work_related_factors table
ALTER TABLE work_related_factors
ADD CONSTRAINT fk_work_related_factors_respondent_id
FOREIGN KEY (respondent_id)
REFERENCES mental_health_survey (respondent_id);

-- Add foreign key constraint to the gender_self_employment_analysis table
ALTER TABLE gender_self_employment_analysis
ADD CONSTRAINT fk_gender_self_employment_analysis_respondent_id
FOREIGN KEY (respondent_id)
REFERENCES mental_health_survey (respondent_id);

-- Add foreign key constraint to the gender_based_analysis table
ALTER TABLE gender_based_analysis
ADD CONSTRAINT fk_gender_based_analysis_respondent_id
FOREIGN KEY (respondent_id)
REFERENCES mental_health_survey (respondent_id);

-- Add foreign key constraint to the country_based_analysis table
ALTER TABLE country_based_analysis
ADD CONSTRAINT fk_country_based_analysis_respondent_id
FOREIGN KEY (respondent_id)
REFERENCES mental_health_survey (respondent_id);

-- Add foreign key constraint to the cleaned_mental_health_data table
ALTER TABLE cleaned_mental_health_data
ADD CONSTRAINT fk_cleaned_mental_health_data_respondent_id
FOREIGN KEY (respondent_id)
REFERENCES mental_health_survey (respondent_id);
