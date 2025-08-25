/*
 * Copyright (c) 2025, WSO2 LLC. (http://www.wso2.com).
 *
 * WSO2 LLC. licenses this file to you under the Apache License,
 * Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

package org.wso2.identity.integration.test.webhooks.usermanagement.eventpayloadbuilder;

import org.json.JSONException;
import org.json.JSONObject;
import org.wso2.carbon.utils.multitenancy.MultitenantConstants;
import org.wso2.identity.integration.test.webhooks.util.EventPayloadUtils;

/**
 * Utility class which builds the expected event payload for admin initiated credential related events.
 */
public class AdminInitCredentialEventTestExpectedEventPayloadBuilder {

    static JSONObject createUserObjectForUserCredentialUpdateWithoutAnyOtherClaims(String userId,
                                                                                   String tenantDomain)
            throws JSONException {

        JSONObject user = new JSONObject();
        user.put("id", userId);

        JSONObject userOrganization = new JSONObject();
        userOrganization.put("id", "dummy-org-id");
        if (tenantDomain.equals(MultitenantConstants.SUPER_TENANT_DOMAIN_NAME)) {
            userOrganization.put("name", "Super");
        } else {
            userOrganization.put("name", tenantDomain);
        }
        userOrganization.put("orgHandle", tenantDomain);
        userOrganization.put("depth", 0);
        user.put("organization", userOrganization);

        if (tenantDomain.equals(MultitenantConstants.SUPER_TENANT_DOMAIN_NAME)) {
            user.put("ref", "https://localhost:9853/scim2/Users/" + userId);
        } else {
            user.put("ref", "https://localhost:9853/t/" + tenantDomain + "/scim2/Users/" + userId);
        }

        return user;
    }

    /**
     * Builds the expected payload for a user credential updated event when neither account state management claims
     * nor other profile claim gets updated in the context of test case.
     *
     * @param userId       ID of the user whose credential is being updated
     * @param tenantDomain Tenant domain of the user
     * @return JSONObject representing the expected user profile updated event payload
     * @throws Exception if an error occurs while building the payload
     */
    public static JSONObject buildExpectedUserCredentialUpdatedEventPayloadWithoutAnyOtherClaims(
            String userId, String tenantDomain) throws Exception {

        JSONObject userProfileUpdateEvent = new JSONObject();

        userProfileUpdateEvent.put("initiatorType", "ADMIN");
        userProfileUpdateEvent.put("user",
                createUserObjectForUserCredentialUpdateWithoutAnyOtherClaims(userId, tenantDomain));
        userProfileUpdateEvent.put("tenant", EventPayloadUtils.createTenantObject(tenantDomain));
        userProfileUpdateEvent.put("organization", EventPayloadUtils.createOrganizationObject(tenantDomain));
        userProfileUpdateEvent.put("userStore", EventPayloadUtils.createUserStoreObject());
        userProfileUpdateEvent.put("action", "CREDENTIAL_UPDATE");
        userProfileUpdateEvent.put("credentialType", "PASSWORD");

        return userProfileUpdateEvent;
    }
}
