package com.abnamro.nl.mobile.payments.core.toggle.feature;


import com.abnamro.nl.toggle.annotation.FeatureToggleBind;
import com.abnamro.nl.toggle.annotation.FeatureToggleConfiguration;

/**
 * Define the feature toggles here, create getters. Because of limitation of annotation processing,
 * they should be defined default or public to be accessible from the binder class. Java beans is not supported yet.
 *
 * create getters for it or just make it public (Why not)
 * expirationDate format is yyyy-MM-dd
 *
 * Use the CoreClassWiring.getFeatureToggles() method to access your toggle.
 */

@FeatureToggleConfiguration(strictnessPolicy = FeatureToggleConfiguration.StrictnessPolicy.MODERATE, maxNumberOfToggles = 15)
public class FeatureToggleConfig {
    //The toggles need to be booleans with at least default accessibility.
    @FeatureToggleBind(toggleName = "SPK-multibanking", expirationDate = "2018-06-15")
    boolean includeMultiBankingFeature = true;
    @FeatureToggleBind(toggleName = "CUOA-OnboardingFeature", expirationDate = "2018-04-30")
    boolean onboardingEnabled = true;
    @FeatureToggleBind(toggleName = "LIZ-QrLogin", expirationDate = "2018-03-31")
    boolean isQrLoginEnabled = true;
    @FeatureToggleBind(toggleName = "SDR-TravelInsurance", expirationDate = "2018-06-30")
    boolean isTravelInsuranceEnabled = true;
    @FeatureToggleBind(toggleName = "LIZ-UbiSettingAwareness", expirationDate = "2018-03-31")
    boolean isUbiSettingAwarenessEnabled = true;
    @FeatureToggleBind(toggleName = "SDR-ChangeLiabilityInsurance", expirationDate =  "2018-06-30")
    boolean isChangeLiabilityInsuranceEnabled = true;
    @FeatureToggleBind(toggleName = "SDR-ViewLiabilityInsuranceDetails", expirationDate =  "2018-06-30")
    boolean isViewLiabilityInsuranceDetailsEnabled = true;

    public boolean isTravelInsuranceEnabled() {
        return isTravelInsuranceEnabled;
    }

    public boolean isChangeLiabilityInsuranceEnabled() {
        return isChangeLiabilityInsuranceEnabled;
    }

    public boolean isViewLiabilityInsuranceDetailsEnabled() {
        return isViewLiabilityInsuranceDetailsEnabled;
    }

    public boolean includeMultiBankingFeature() {
        return includeMultiBankingFeature;
    }

    public boolean isOnboardingEnabled() {
        return onboardingEnabled;
    }

    public boolean isQrLoginEnabled() {
        return isQrLoginEnabled;
    }

    public boolean isUbiSettingAwarenessEnabled() { return isUbiSettingAwarenessEnabled; }
}
