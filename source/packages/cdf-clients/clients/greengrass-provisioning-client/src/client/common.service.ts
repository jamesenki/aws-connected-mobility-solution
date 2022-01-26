/*--------------------------------------------------------------------------------------------------------------------
#  Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.                                           *
#                                                                                                                    *
#  Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance    *
#  with the License. A copy of the License is located at                                                             *
#                                                                                                                    *
#      http://www.apache.org/licenses/LICENSE-2.0                                                                    *
#                                                                                                                    *
#  or in the 'license' file accompanying this file. This file is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES *
#  OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions    *
#  and limitations under the License.                                                                                *
#-------------------------------------------------------------------------------------------------------------------*/
/**
 * Connected Device Framework: Dashboard Facade
 * Asset Library implementation of DevicesService *
 */

import { injectable } from 'inversify';
import config from 'config';
import {RequestHeaders} from './common.model';

@injectable()
export abstract class ClientServiceBase  {

    protected MIME_TYPE:string = 'application/vnd.aws-cdf-v1.0+json';

    private readonly _headers:RequestHeaders = {
        'Accept': this.MIME_TYPE,
        'Content-Type': this.MIME_TYPE
    };

    protected buildHeaders(additionalHeaders:RequestHeaders) {

        let headers = Object.assign({}, this._headers);

        if (config.has('greengrassProvisioning.headers')) {
            const headersFromConfig:RequestHeaders = config.get('greengrassProvisioning.headers') as RequestHeaders;
            if (headersFromConfig !== null && headersFromConfig !== undefined) {
                headers = {...headers, ...headersFromConfig};
            }
        }

        if (additionalHeaders !== null && additionalHeaders !== undefined) {
            headers = {...headers, ...additionalHeaders};
        }

        const keys = Object.keys(headers);
        keys.forEach(k=> {
            if (headers[k]===undefined || headers[k]===null) {
                delete headers[k];
            }
        });

        return headers;
    }

}
